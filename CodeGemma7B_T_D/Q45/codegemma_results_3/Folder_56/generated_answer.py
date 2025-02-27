from itertools import permutations

def palindromes_between_indices(text):
    return set((p for p in permutations(text[5:10]) if p == p[::-1] and len(p) >= 5))