from itertools import permutations

def palindromes_between_indices(text):
    letters = ''.join((c for c in text[4:10] if c.isalpha()))
    return {''.join(p) for p in permutations(letters) if ''.join(p).lower() == ''.join(p)[::-1].lower() and len(''.join(p)) >= 6}