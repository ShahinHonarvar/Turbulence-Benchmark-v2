from itertools import permutations

def palindromes_between_indices(s):
    substring = ''.join(filter(str.isalpha, s[1:9])).lower()
    perms = set((''.join(p) for p in permutations(substring) if len(p) >= 6))
    return {p for p in perms if p == p[::-1] and len(p) >= 6}