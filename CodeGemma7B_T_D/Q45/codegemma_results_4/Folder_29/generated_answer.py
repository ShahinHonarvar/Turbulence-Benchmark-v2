from itertools import permutations
from string import ascii_letters

def palindromes_between_indices(text):
    lst = [c for c in text[2:10] if c.lower() in ascii_letters]
    if not lst:
        return set()
    return {''.join(p) for p in permutations(lst, len(lst)) if p == p[::-1]}