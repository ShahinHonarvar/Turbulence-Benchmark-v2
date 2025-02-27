def palindromes_between_indices(text):
    letters = ''.join((c for c in text[:4] if c.isalpha())).lower()
    return {word for word in set(permutations(letters)) if len(word) >= 3 and word == word[::-1]}