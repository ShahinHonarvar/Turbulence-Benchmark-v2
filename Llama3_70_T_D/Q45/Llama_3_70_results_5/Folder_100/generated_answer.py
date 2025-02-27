from itertools import permutations

def palindromes_between_indices(s):
    s = s[:6].lower()
    letters = sorted([c for c in s if c.isalpha()])
    return set((''.join(p) for r in range(6, 0, -1) for p in permutations(letters, r) if p == p[::-1]))