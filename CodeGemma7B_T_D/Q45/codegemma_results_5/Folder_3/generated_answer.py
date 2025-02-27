from itertools import permutations

def palindromes_between_indices(string):
    s = set()
    for p in permutations(string[7:10]):
        s.add(''.join(p).lower())
    return s