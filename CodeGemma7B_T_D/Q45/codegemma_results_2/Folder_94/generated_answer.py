from itertools import permutations

def palindromes_between_indices(text):
    return {''.join(p) for p in permutations(text[3:5].lower()) if p == p[::-1]}