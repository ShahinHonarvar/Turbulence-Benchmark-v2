import itertools

def palindromes_between_indices(s):
    letters = [''.join(p) for i in range(3, len(s) + 1) for p in itertools.permutations(s[6:10]) if p == p[::-1]]
    return set(filter(lambda x: len(x) >= 3, letters))