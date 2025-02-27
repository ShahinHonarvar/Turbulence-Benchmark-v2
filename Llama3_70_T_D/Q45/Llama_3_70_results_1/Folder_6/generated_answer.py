from collections import Counter
from itertools import permutations

def palindromes_between_indices(s):
    s = s[:8].lower()
    counter = Counter((c for c in s if c.isalpha()))
    palindromes = set()
    for r in range(4, sum(counter.values()) + 1):
        for p in permutations(counter.elements(), r):
            if p == p[::-1]:
                palindromes.add(''.join(p))
    return palindromes