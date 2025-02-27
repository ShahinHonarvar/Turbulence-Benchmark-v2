from collections import Counter
from itertools import permutations

def palindromes_between_indices(s):
    s = s[1:8].lower()
    counter = Counter((c for c in s if c.isalpha()))
    palindromes = set()
    for r in range(5, len(s) + 1):
        for p in permutations(s, r):
            word = ''.join(p)
            if word == word[::-1]:
                if Counter((c for c in word)).items() <= counter.items():
                    palindromes.add(word)
    return palindromes