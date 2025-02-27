from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(s):
        return s == s[::-1]
    substring = ''.join((c for c in s[3:9] if c.isalpha())).lower()
    perms = set((''.join(p) for i in range(4, len(substring) + 1) for p in permutations(substring, i)))
    palindromes = {p for p in perms if is_palindrome(p)}
    return palindromes