from itertools import permutations
from string import ascii_letters

def palindromes_between_indices(text):
    text = text[5:7]
    return {''.join(p) for p in permutations(text) if text == text[::-1]}