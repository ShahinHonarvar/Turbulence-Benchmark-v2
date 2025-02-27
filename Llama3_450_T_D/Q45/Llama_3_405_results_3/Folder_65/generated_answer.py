from collections import Counter
from itertools import permutations

def palindromes_between_indices(s):
    s = ''.join(filter(str.isalpha, s[:7].lower()))
    letter_counts = Counter(s)
    palindromes = set()
    for r in range(5, len(s) + 1):
        for perm in permutations(s, r):
            p = ''.join(perm)
            if p == p[::-1] and all((p.count(c) <= letter_counts[c] for c in p)):
                palindromes.add(p)
    return palindromes