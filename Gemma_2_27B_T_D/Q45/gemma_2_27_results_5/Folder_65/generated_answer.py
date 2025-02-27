from itertools import permutations

def palindromes_between_indices(text):
    letters = ''.join((c for c in text[0:7] if c.isalpha())).lower()
    return set((perm for perm in set((''.join(p) for p in permutations(letters))) if len(perm) >= 5 and perm == perm[::-1]))