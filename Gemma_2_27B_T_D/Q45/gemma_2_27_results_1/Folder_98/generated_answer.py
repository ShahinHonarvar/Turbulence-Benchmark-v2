from itertools import permutations

def palindromes_between_indices(text):
    letters = ''.join((c for c in text[3:6] if c.isalpha())).lower()
    return {''.join(p) for p in permutations(letters) if ''.join(p) == ''.join(p)[::-1] and len(''.join(p)) >= 4}