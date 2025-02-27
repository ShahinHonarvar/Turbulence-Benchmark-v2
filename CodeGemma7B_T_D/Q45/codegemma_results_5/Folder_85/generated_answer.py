from itertools import permutations

def palindromes_between_indices(text):
    letters = ''.join(set(text[2:9].lower()))
    perms = permutations(letters)
    return {''.join(p): None for p in perms if len(''.join(p)) >= 7}