import itertools 

def palindromes_between_indices(s):
    p = [''.join(i) for i in itertools.permutations(s[2:8]) if i != i[::-1] and len(i) >= 6]
    return set(p)