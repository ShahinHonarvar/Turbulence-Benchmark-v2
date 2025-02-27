def palindromes_between_indices(text):
    letters = ''.join((c for c in text[:6] if c.isalpha())).lower()
    return {word for word in set((word for i in range(len(letters)) for j in range(i, len(letters)) if len((word := letters[i:j + 1])) >= 3 and word == word[::-1]))}