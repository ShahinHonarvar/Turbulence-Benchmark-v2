from itertools import permutations

def is_palindrome(s):
    return s == s[::-1]

def palindromes_between_indices(s):
    s = s.lower()
    if len(s) < 6:
        return set()
    chars = [c for c in s[3:6] if c.isalpha()]
    if len(chars) < 4:
        return set()
    perm_set = set((''.join(p) for p in permutations(chars, 4)))
    return {p for p in perm_set if is_palindrome(p)}