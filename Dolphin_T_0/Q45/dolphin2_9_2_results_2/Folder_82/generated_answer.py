from itertools import permutations, chain
import re

def palindromes_between_indices(s):
    letters = chain.from_iterable(permutations(s[1:7], 7))
    return {w for w in letters if len(w) >= 7 and w.lower() == w[::-1].lower()}