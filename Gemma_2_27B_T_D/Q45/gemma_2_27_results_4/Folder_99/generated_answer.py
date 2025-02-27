def palindromes_between_indices(text):
    letters = ''.join((c for c in text[4:9] if c.isalpha())).lower()
    return set((p for p in {''.join(p) for p in permutations(letters) if len(p) >= 3} if p == p[::-1]))