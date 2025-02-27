def palindromes_between_indices(text):
    letters = ''.join((c for c in text[:4] if c.isalpha())).lower()
    return {word for word in set((''.join(p) for p in permutations(letters))) if len(word) >= 4 and word == word[::-1]}