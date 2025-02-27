from itertools import permutations

def palindromes_between_indices(text):
    letters = ''.join((c.lower() for c in text[1:7] if c.isalpha()))
    return set((''.join(p) for p in permutations(letters) if len(p) >= 3))