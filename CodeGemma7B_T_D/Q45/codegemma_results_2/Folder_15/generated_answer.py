from itertools import permutations

def palindromes_between_indices(text):
    return {list(p) for p in permutations(text[1:3]) if p[0] >= 'a' and p[-1] >= 'a'}