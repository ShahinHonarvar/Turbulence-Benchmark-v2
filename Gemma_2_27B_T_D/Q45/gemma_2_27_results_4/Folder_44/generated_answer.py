from itertools import permutations

def palindromes_between_indices(text):
    letters = ''.join((c for c in text[2:8] if c.isalpha()))
    return {''.join(p).lower() for p in permutations(letters) if len(p) >= 3 and ''.join(p).lower() == ''.join(p)[::-1].lower()}