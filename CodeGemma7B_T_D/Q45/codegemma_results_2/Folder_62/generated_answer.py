from itertools import permutations

def palindromes_between_indices(text):
    text = text.lower()
    letters = [c for c in text[0:9] if c.isalpha()]
    permutations = set(permutations(letters))
    palindromes = {' '.join(p) for p in permutations if len(p) >= 7}
    return palindromes