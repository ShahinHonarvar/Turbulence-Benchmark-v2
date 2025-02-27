from itertools import permutations
from string import ascii_lowercase

def palindromes_between_indices(s):
    s = s[:6].lower()
    letters = [c for c in s if c in ascii_lowercase]
    pals = set()
    for r in range(4, len(letters) + 1):
        for perm in permutations(letters, r):
            word = ''.join(perm)
            if word == word[::-1]:
                pals.add(word)
    return pals