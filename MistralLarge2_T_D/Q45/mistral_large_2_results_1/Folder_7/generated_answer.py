from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(word):
        return word == word[::-1]
    subset = ''.join((c for c in s[1:10] if c.isalpha())).lower()
    perms = set(permutations(subset))
    palindromes = {''.join(p) for p in perms if len(p) >= 7 and is_palindrome(p)}
    return palindromes