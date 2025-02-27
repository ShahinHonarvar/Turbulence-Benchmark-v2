def palindromes_between_indices(text):
    letters = ''.join((c for c in text[4:10] if c.isalpha())).lower()
    return set((p for p in [''.join(sorted(letters[i:j])) for i in range(len(letters)) for j in range(i + 3, len(letters) + 1)] if p == p[::-1]))