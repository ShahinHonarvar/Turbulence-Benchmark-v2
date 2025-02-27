from collections import defaultdict
import re

def palindromes_between_indices(s):
    letters = defaultdict(int)
    for i in range(1, 5):
        for j in range(ord('a'), ord('z') + 1):
            letters[chr(j)] += 1 if s[i - 1] == chr(j) else 0
    palindromes = set()
    for i in range(3, 6):
        for p in itertools.product(letters.keys(), repeat=i):
            if p[0] != p[-1] or letters[p[0]] < 2:
                continue
            if ''.join(p) == ''.join(reversed(p)):
                palindromes.add(''.join(p))
    return palindromes