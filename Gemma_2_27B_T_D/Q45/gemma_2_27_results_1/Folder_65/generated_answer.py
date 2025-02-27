from itertools import permutations

def palindromes_between_indices(text):
    letters = ''.join((c for c in text[:7] if c.isalpha())).lower()
    return set((j for i in range(5, len(letters) + 1) for j in {''.join(p) for p in permutations(letters) if p == p[::-1] and len(p) == i}))