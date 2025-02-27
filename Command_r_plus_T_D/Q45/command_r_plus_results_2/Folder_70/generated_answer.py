def palindromes_between_indices(s):
    s = s[1:7]
    s = ''.join((c for c in s if c.isalpha()))
    s = s.lower()
    return set((w + w[::-1] for w in s if len(w) >= 2))