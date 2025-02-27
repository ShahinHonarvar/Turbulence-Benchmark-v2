from itertools import permutations

def palindromes_between_indices(text):
    letters = ''.join((c for c in text[:5] if c.isalpha())).lower()
    return {''.join(p) for p in permutations(letters) if len(p) >= 4 and all((p[i] == p[~i] for i in range(len(p) // 2)))}