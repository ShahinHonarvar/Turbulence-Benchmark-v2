def palindromes_between_indices(text):
    letters = ''.join((c for c in text[3:8] if c.isalpha())).lower()
    return {word for word in set(permutations(letters)) if len(word) >= 4 and word == word[::-1]}