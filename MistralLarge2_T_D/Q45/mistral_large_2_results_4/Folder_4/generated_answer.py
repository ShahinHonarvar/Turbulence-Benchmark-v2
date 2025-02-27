from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(word):
        return word == word[::-1]
    s = s[3:10]
    s = ''.join(filter(str.isalpha, s)).lower()
    palindromes = set()
    for length in range(7, len(s) + 1):
        for perm in permutations(s, length):
            word = ''.join(perm)
            if is_palindrome(word):
                palindromes.add(word)
    return palindromes