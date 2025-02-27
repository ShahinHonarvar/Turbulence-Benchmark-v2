def palindromes_between_indices(string):
    letters = ''.join((c for c in string[2:8] if c.isalpha())).lower()
    return {''.join(p) for i in range(3, len(letters) + 1) for p in itertools.permutations(letters, i) if p == tuple(reversed(p))}