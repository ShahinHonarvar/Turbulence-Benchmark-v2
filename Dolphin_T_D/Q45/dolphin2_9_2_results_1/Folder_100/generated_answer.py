def palindromes_between_indices(s):
    letters = ''.join(sorted([c for c in s[:6] if c.isalpha()]))
    return set((i for i in (''.join(p) for p in itertools.permutations(letters, 6)) if i == i[::-1].lower()))