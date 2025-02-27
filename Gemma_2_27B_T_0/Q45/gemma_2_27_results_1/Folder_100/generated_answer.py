from itertools import permutations

def palindromes_between_indices(text):
    letters = ''.join((c for c in text[:6] if c.isalpha())).lower()
    return {''.join(p) for p in permutations(letters) if len(p) >= 6 and ''.join(p) == ''.join(p)[::-1]}