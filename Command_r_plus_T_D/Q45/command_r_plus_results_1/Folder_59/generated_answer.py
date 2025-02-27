def palindromes_between_indices(s):
    s = s[8:10].lower()
    return set((w for w in s.upper() + s.lower() if s.count(w) > 1))