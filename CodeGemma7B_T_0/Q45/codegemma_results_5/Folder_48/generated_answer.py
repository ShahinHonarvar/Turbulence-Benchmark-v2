def palindromes_between_indices(text):
    text = text.lower()
    text = text[6:9]
    if not text.isalpha():
        return set()
    return {''.join(p) for p in itertools.permutations(text)}