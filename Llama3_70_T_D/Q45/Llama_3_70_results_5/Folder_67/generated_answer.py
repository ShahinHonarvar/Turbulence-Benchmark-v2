import itertools

def palindromes_between_indices(s):
    letters = set((c.lower() for c in s[2:7] if c.isalpha()))
    pals = set()
    for p in itertools.permutations(letters, 5):
        w = ''.join(p)
        if w == w[::-1]:
            pals.add(w)
    return pals