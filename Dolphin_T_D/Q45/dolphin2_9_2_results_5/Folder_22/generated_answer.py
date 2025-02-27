def palindromes_between_indices(s):
    letters = ''.join((c.lower() for c in s[5:7] if c.isalpha()))
    return set((p for p in (''.join((c for c in sorted(letters)))[i:j + 1] for i in range(len(letters)) for j in range(i + 2, len(letters))) if p == p[::-1]))