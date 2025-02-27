def palindromes_between_indices(s):
    letters = [c for c in s[6:10] if c.isalpha()]
    return set((p for p in (''.join(p) for i in range(5, len(letters) + 1) for p in permutations(letters, i) if p == p[::-1]) if len(p) >= 5))