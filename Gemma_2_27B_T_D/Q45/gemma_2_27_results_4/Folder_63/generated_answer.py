def palindromes_between_indices(text):
    letters = ''.join((c for c in text[0:4] if c.isalpha())).lower()
    return set((word for word in {''.join(permutation) for permutation in itertools.permutations(letters)} if len(word) >= 3 and word == word[::-1]))