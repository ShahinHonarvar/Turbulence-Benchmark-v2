def palindromes_between_indices(text):
    letters = ''.join((c for c in text[1:8] if c.isalpha())).lower()
    return {word for word in set([''.join(p) for p in itertools.permutations(letters)]) if len(word) >= 3 and word == word[::-1]}