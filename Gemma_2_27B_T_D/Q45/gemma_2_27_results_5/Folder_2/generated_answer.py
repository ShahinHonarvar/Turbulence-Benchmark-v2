from itertools import permutations

def palindromes_between_indices(text):
    letters = text[1:6].lower()
    return set((p for p in (''.join(perm) for perm in permutations(letters)) if p == p[::-1] and len(p) >= 6))