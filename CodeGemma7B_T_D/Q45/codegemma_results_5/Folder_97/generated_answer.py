import itertools

def palindromes_between_indices(text):
    letters = set(filter(str.isalpha, text[0:5].lower()))
    return {''.join(p) for p in itertools.permutations(letters, len(letters)) if len(p) >= 3}