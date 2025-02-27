import string
from itertools import permutations

def palindromes_between_indices(s):
    letters = [c for c in s if c in string.ascii_letters]
    pals = set()
    for p in permutations(letters, len(letters)):
        for i in range(len(p) - 3):
            for j in range(i + 3, len(p) + 1):
                pal = ''.join(p[i:j]).lower()
                if pal == pal[::-1] and j - i >= 4:
                    pals.add(pal)
    return pals