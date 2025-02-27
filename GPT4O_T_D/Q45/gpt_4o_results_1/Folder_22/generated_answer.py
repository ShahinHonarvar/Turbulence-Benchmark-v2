from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(word):
        return word == word[::-1]
    middle = s[5:7].lower()
    if len(middle) < 2:
        return set()
    palindromes = set()
    for length in range(3, 4):
        for perm in permutations(middle, length):
            perm_str = ''.join(perm)
            if is_palindrome(perm_str):
                palindromes.add(perm_str)
    return palindromes