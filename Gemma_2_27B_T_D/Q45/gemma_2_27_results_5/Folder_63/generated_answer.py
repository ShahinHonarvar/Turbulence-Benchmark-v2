def palindromes_between_indices(s):
    letters = ''.join((c for c in s[0:4] if c.isalpha())).lower()
    return {p for p in set((p for p in [''.join(p) for p in [[''.join(sorted(list(letters)[i:j])) for j in range(i + 3, len(letters) + 1)] for i in range(len(letters))]])) if len(p) >= 3 and p == p[::-1]}