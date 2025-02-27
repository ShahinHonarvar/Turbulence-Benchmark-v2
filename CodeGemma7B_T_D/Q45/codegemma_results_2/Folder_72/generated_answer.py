from collections import defaultdict
from itertools import permutations
from string import ascii_lowercase

def palindromes_between_indices(s):
    p = defaultdict(set)
    for w in permutations((i for i in s[1:8] if i.lower() in ascii_lowercase)):
        for j in range(len(w) - 5):
            for k in range(j + 6, len(w) + 1):
                p[j, k].add(''.join(w[j:k]))
    return p