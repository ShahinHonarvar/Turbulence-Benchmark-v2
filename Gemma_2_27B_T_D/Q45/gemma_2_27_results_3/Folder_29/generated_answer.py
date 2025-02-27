from itertools import permutations

def palindromes_between_indices(text):
    letters = ''.join((c for c in text[2:10] if c.isalpha())).lower()
    return set((perm for perm in (''.join(p) for p in permutations(letters)) if len(perm) >= 6 and perm == perm[::-1]))