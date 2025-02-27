def palindromes_between_indices(text):
    letters = ''.join((c for c in text[1:8] if c.isalpha())).lower()
    return {word for word in set(permutations(letters)) if word == word[::-1] and len(word) >= 3}