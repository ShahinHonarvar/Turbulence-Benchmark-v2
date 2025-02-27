def palindromes_between_indices(s: str) -> set:
    s = s[:7]
    s = ''.join((c for c in s if c.isalpha()))
    s = s.lower()
    return set((w for w in s if s.count(w) > 1 and len(w) >= 3))