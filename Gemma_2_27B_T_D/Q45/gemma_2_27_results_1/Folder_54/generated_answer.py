from itertools import permutations

def palindromes_between_indices(text):
    letters = ''.join((c for c in text[4:10] if c.isalpha())).lower()
    return {''.join(p) for p in permutations(letters) if len(p) >= 4 and p == p[::-1]}