from itertools import permutations

def palindromes_between_indices(text):
    letters = ''.join((c for c in text[4:9] if c.isalpha())).lower()
    return set([''.join(p) for p in permutations(letters) if p == p[::-1] and len(p) >= 3])