from itertools import permutations

def palindromes_between_indices(text):
    letters = ''.join(text[1:6]).lower()
    candidates = set((p for p in permutations(letters) if len(p) >= 6 and p == p[::-1]))
    return {''.join(candidate) for candidate in candidates}