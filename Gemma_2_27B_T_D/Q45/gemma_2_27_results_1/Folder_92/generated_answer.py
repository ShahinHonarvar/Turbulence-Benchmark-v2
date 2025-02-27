from itertools import permutations

def palindromes_between_indices(text):
    letters = ''.join((c for c in text[4:8] if c.isalpha())).lower()
    return set((p for p in (''.join(perm) for perm in permutations(letters)) if len(p) >= 4 and p == p[::-1]))