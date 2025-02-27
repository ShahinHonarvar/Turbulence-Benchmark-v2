from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(word):
        return word == word[::-1]
    substring = ''.join((c for c in s[1:8] if c.isalpha())).lower()
    palindromes = set()
    for r in range(3, len(substring) + 1):
        for perm in permutations(substring, r):
            word = ''.join(perm)
            if is_palindrome(word):
                palindromes.add(word)
    return palindromes