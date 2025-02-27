def palindromes_between_indices(text):
    letters = ''.join((c for c in text[:5] if c.isalpha()))
    return set((p for p in {''.join(p) for p in permutations(letters)} if len(p) >= 3 and p.lower() == p.lower()[::-1]))