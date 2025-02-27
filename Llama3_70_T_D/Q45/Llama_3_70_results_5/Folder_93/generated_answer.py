from itertools import permutations
import string

def palindromes_between_indices(s):
    s = s[2:8].lower()
    s = ''.join((c for c in s if c in string.ascii_lowercase))
    pals = set()
    for r in range(6, len(s) + 1):
        for perm in permutations(s, r):
            word = ''.join(perm)
            if word == word[::-1]:
                pals.add(word)
    return pals