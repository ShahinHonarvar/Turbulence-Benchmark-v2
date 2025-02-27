from itertools import permutations

def palindromes_between_indices(string):
    return {''.join(p) for p in permutations(string[5:10].lower()) if p[0] >= 'a' and p[-1] >= 'a'}