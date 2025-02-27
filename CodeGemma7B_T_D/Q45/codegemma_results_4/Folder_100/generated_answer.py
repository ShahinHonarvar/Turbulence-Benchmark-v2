from itertools import permutations

def palindromes_between_indices(s):
    g = list(permutations(s[0:6]))
    return {(i, j): ''.join(i).lower() for i, j in g if len(i) >= 6}