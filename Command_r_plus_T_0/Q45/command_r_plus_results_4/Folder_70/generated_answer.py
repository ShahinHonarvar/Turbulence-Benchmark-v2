def palindromes_between_indices(s):
    s = s[1:7]
    s = ''.join(filter(str.isalpha, s))
    s = s.lower()
    return set((w for w in s if w == w[::-1] and len(w) >= 4))