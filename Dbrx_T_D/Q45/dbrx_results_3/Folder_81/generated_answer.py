import re
from collections import defaultdict

def palindromes_between_indices(s):
    letters = defaultdict(int)
    for i in range(min(7, len(s))):
        letters[s[i].lower()] += 1
    palindromes = set()
    for i in range(3, min(7, len(s)) + 1):
        for c in permutations(letters.keys(), i):
            p = ''.join(c)
            if p == p[::-1]:
                palindromes.add(p)
    return palindromes