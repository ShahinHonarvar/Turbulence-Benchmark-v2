def palindromes_between_indices(text):
    letters = ''.join((c for c in text[1:7] if c.isalpha())).lower()
    return {word for word in set(letters) if len(word) >= 4 and word == word[::-1]}