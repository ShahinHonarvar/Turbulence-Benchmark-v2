from itertools import permutations

def palindromes_between_indices(text):
    letters = ''.join((c for c in text[3:7] if c.isalpha())).lower()
    return {''.join(p) for p in set(permutations(letters)) if len(p) >= 3 and p == p[::-1]}