from collections import Counter
from itertools import permutations

def palindromes_between_indices(s):
    s = s[2:10].lower()
    s = ''.join(filter(str.isalpha, s))
    counter = Counter(s)
    palindromes = set()
    for r in range(7, len(s) + 1):
        for perm in permutations(s, r):
            perm_str = ''.join(perm)
            if perm_str == perm_str[::-1] and all((counter[c] >= perm_str.count(c) for c in set(perm_str))):
                palindromes.add(perm_str)
    return palindromes