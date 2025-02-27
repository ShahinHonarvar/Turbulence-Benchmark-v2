import itertools
from collections import Counter

def palindromes_between_indices(s):
    s = ''.join(filter(str.isalpha, s[:6].lower()))
    counter = Counter(s)
    letters = ''.join(counter.elements())
    palindromes = set()
    for r in range(4, len(letters) + 1):
        for p in itertools.permutations(letters, r):
            p = ''.join(p)
            if p == p[::-1]:
                palindromes.add(p)
    return palindromes