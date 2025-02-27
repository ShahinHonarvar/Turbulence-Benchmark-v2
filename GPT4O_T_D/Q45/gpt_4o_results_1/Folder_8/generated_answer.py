from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(word):
        return word == word[::-1]
    if len(s) < 6:
        return set()
    substring = ''.join(filter(str.isalpha, s[1:6])).lower()
    palindromes_set = set()
    for length in range(5, len(substring) + 1):
        for perm in permutations(substring, length):
            word = ''.join(perm)
            if is_palindrome(word):
                palindromes_set.add(word)
    return palindromes_set