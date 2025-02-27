from itertools import permutations

def palindromes_between_indices(text):
    letters = ''.join((char for char in text[3:6] if char.isalpha())).lower()
    if len(letters) < 3:
        return set()
    return {''.join(p) for p in permutations(letters)}