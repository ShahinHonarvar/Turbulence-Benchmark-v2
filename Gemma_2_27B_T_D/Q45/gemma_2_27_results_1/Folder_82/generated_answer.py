from itertools import permutations

def palindromes_between_indices(text):
    letters = ''.join((c for c in text[1:7] if c.isalpha())).lower()
    return {''.join(p) for p in permutations(letters) if len(''.join(p)) >= 7 and ''.join(p) == ''.join(p)[::-1]}