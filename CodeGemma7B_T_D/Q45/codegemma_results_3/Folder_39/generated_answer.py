from itertools import permutations

def palindromes_between_indices(s):
    p = [''.join(p) for p in permutations(s[2:6])]
    return set([c for c in p if c == c[::-1]])