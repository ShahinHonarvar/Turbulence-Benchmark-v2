from itertools import permutations

def palindromes_between_indices(text):
    letters = ''.join((c for c in text[6:10] if c.isalpha()))
    permutations_set = set((''.join(p) for p in permutations(letters.lower())))
    return {p for p in permutations_set if len(p) >= 5 and p == p[::-1]}