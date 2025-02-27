from itertools import permutations

def palindromes_between_indices(s):
    substring = ''.join((c.lower() for c in s[3:8] if c.isalpha()))
    if len(substring) < 6:
        return set()
    perms = set((''.join(p) for p in permutations(substring) if is_palindrome(p)))
    return {p for p in perms if len(p) >= 6}

def is_palindrome(s):
    return s == s[::-1]