from itertools import permutations

def palindromes_between_indices(s):
    s = s[5:10].lower()
    letters = [c for c in s if c.isalpha()]
    pals = set()
    for r in range(5, len(letters) + 1):
        for p in permutations(letters, r):
            w = ''.join(p)
            if w == w[::-1]:
                pals.add(w)
    return pals