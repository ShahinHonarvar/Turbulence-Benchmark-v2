def palindromes_between_indices(s):
    s = s[6:10].lower()
    return set((w for w in s.lower() if w == w[::-1] and len(w) >= 3 and w.isalpha()))