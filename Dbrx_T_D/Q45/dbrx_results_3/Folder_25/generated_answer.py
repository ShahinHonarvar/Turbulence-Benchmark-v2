from functools import reduce
from itertools import combinations

def palindromes_between_indices(s):
    letters = set(s.lower()[1:5]) & set('abcdefghijklmnopqrstuvwxyz')
    return set(reduce(lambda x, y: x | y, ([p + ''.join(c) + p[::-1] for p in letters for c in combinations(letters - set(p), n)] for n in range(1, 5))))