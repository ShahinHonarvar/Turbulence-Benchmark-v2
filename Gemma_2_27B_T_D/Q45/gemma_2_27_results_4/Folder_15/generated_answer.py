def palindromes_between_indices(text):
    letters = ''.join((c for c in text[1:3] if c.isalpha())).lower()
    return set((p for p in {''.join(p) for i in range(len(letters)) for p in permutations(letters, i + 1) if ''.join(p) == ''.join(p)[::-1] and len(p) >= 3} if p.isalpha()))