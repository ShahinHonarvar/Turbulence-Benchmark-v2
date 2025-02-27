import itertools

def palindromes_between_indices(s):
    s = s[4:9].lower()
    chars = set((c for c in s if c.isalpha()))
    return {p for i in range(5, len(s) + 1) for p in (''.join(c) for c in itertools.permutations(chars, i)) if p == p[::-1]}