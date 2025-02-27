def palindromes_between_indices(text):
    letters = ''.join((c for c in text[3:6] if c.isalpha())).lower()
    return {word for word in set(''.join((letters[p:p + i] for p in range(len(letters)) for i in range(1, len(letters) - p + 1)))) if len(word) >= 3 and word == word[::-1]}