import itertools
from collections import Counter

def palindromes_between_indices(s):
    s = s[:6].lower()
    s = ''.join(filter(str.isalpha, s))
    counter = Counter(s)
    palindromes = set()
    for r in range(3, len(s) + 1):
        for combo in itertools.combinations(s, r):
            if len(combo) >= 3:
                for perm in itertools.permutations(combo):
                    p = ''.join(perm)
                    if p == p[::-1] and len(p) >= 6:
                        palindromes.add(p)
    return palindromes