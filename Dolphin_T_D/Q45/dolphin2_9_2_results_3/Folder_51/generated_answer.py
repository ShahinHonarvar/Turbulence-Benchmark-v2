from itertools import permutations

def palindromes_between_indices(s):
    pals = set()
    letters = [c for c in s[3:6] if c.isalpha()]
    if len(letters) < 3:
        return pals
    for p in permutations(letters, 3):
        pal = ''.join(p)
        if pal == pal[::-1]:
            pals.add(pal.lower())
    return pals