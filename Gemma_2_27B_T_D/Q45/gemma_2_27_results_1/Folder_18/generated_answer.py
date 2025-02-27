def palindromes_between_indices(text):
    letters = ''.join((c for c in text[1:7] if c.isalpha())).lower()
    return set((p for p in {''.join(sorted(w)) for w in [letters[i:i + j] for j in range(3, len(letters) + 1) for i in range(len(letters) - j + 1)]} if p == p[::-1]))