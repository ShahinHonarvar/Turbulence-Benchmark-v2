def palindromes_between_indices(s):
    letters = ''.join((c for c in s[:7].lower() if c.isalpha()))
    return set((p for p in {p for i in range(len(letters)) for j in range(i + 2, len(letters) + 1) for p in [letters[i:j]] if p == p[::-1]} if len(p) >= 3))