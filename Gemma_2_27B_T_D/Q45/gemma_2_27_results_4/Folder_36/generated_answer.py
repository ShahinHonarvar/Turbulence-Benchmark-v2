def palindromes_between_indices(text):
    letters = ''.join((c for c in text[5:9] if c.isalpha())).lower()
    return set((p for p in {''.join(reversed(p)) for p in permutations(letters)} if len(p) >= 3 and p == ''.join(reversed(p))))