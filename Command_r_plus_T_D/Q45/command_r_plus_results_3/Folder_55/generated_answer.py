def palindromes_between_indices(s):
    s = s[:3]
    s = ''.join((c for c in s if c.isalpha()))
    s = s.lower()
    return set((w + w[::-1][1:] for w in s))