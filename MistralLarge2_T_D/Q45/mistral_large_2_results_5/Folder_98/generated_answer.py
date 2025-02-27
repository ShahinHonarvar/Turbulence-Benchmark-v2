from itertools import permutations

def palindromes_between_indices(s):
    letters = ''.join((c for c in s[3:6] if c.isalpha())).lower()
    perms = set((''.join(p) for i in range(4, len(letters) + 1) for p in permutations(letters, i)))
    return {p for p in perms if p == p[::-1]}