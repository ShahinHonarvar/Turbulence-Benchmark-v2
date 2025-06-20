from itertools import permutations

def palindromes_between_indices(text):
    letters = ''.join((c for c in text[3:9] if c.isalpha())).lower()
    return {''.join(p) for p in permutations(letters) if len(p) >= 7 and ''.join(p) == ''.join(p)[::-1]}