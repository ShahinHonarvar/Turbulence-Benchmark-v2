import itertools

def palindromes_between_indices(string):
    letters = ''.join((c for c in string[1:4] if c.isalpha())).lower()
    permutations = set([''.join(p) for p in itertools.permutations(letters)])
    return set((p for p in permutations if len(p) >= 4 and p == p[::-1]))