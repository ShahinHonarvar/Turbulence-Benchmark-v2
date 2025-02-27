from itertools import permutations

def is_palindrome(s):
    return s == s[::-1]

def palindromes_between_indices(s):
    substring = ''.join((c.lower() for c in s[2:10] if c.isalpha()))
    perms = set((''.join(p) for p in permutations(substring, len(substring)) if is_palindrome(''.join(p))))
    return {p for p in perms if len(p) >= 6}