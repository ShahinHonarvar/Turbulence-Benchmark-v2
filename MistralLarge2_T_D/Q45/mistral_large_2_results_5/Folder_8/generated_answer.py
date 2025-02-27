from itertools import permutations

def palindromes_between_indices(s):
    chars = [c for c in s[1:6] if c.isalpha()]
    perms = set((''.join(p) for i in range(5, len(chars) + 1) for p in permutations(chars, i)))
    return {p for p in perms if p.lower() == p.lower()[::-1]}