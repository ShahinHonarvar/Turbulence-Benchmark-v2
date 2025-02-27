from itertools import permutations
import re

def palindromes_between_indices(s):
    letters = ''.join(sorted([c for c in s[2:10] if c.isalpha()]))
    palindromes = set()
    for i in range(len(letters)):
        for p in permutations(letters, i + 3):
            word = ''.join(p).lower()
            if word == word[::-1] and len(word) >= 3:
                palindromes.add(word)
    return palindromes