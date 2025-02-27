def palindromes_between_indices(text):
    letters = ''.join((c for c in text[:3] if c.isalpha())).lower()
    return {word for word in set((letters[i:j] for i in range(len(letters)) for j in range(i + 3, len(letters) + 1))) if word == word[::-1]}