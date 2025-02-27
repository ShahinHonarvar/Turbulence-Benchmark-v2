from itertools import permutations
import string

def palindromes_between_indices(s):
    result = set()
    if len(s) >= 10:
        substring = ''.join((c for c in s[4:10] if c in string.ascii_lowercase)).lower()
        perms = [''.join(p) for p in permutations(substring)]
        result = set((p for p in perms if p == p[::-1] and len(p) >= 5))
    return result