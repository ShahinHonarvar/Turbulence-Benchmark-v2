def palindromes_between_indices(s):
    letters = ''.join((c for c in s[6:10] if c.isalpha())).lower()
    return {p for p in set((p for l in range(len(letters)) for p in [letters[i:l + 1] + letters[l:i:-1] for i in range(l + 1)] if len(p) >= 4)) if p == p[::-1]}