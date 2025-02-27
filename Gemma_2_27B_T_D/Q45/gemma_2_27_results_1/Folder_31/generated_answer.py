from itertools import permutations

def palindromes_between_indices(text):
    letters = ''.join((c.lower() for c in text[1:9] if c.isalpha()))
    return {''.join(p) for p in permutations(letters) if len(p) >= 6 and ''.join(p) == ''.join(p)[::-1]}