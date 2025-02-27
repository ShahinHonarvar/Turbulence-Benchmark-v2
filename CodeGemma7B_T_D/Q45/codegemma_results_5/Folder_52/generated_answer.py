from itertools import permutations

def palindromes_between_indices(str):
    return {''.join(p) for p in permutations(str[0:8].lower()) if len(p) > 5}