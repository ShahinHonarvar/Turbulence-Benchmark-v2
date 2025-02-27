def palindromes_between_indices(text):
    letters = ''.join((c for c in text[4:9] if c.isalpha())).lower()
    return {''.join(reversed(word)) for word in set((word for word in ''.join((letters[i:i + len(letters)] for i in range(len(letters)))) if len(word) >= 4 and word == word[::-1]))}