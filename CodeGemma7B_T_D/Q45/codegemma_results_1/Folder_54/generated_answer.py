from itertools import permutations

def palindromes_between_indices(string):
    letters = [char.lower() for char in string[4:10]]
    return {''.join(p) for p in permutations(letters) if len(p) >= 4}