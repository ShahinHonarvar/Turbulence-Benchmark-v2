from itertools import permutations
import re

def palindromes_between_indices(s):
    s = s[6:9].lower()
    s = re.sub('[^a-z]', '', s)
    palindromes = set()
    for r in range(4, len(s) + 1):
        for p in permutations(s, r):
            word = ''.join(p)
            if word == word[::-1]:
                palindromes.add(word)
    return palindromes