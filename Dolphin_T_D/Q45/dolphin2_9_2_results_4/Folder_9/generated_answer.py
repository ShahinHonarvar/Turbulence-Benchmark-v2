from itertools import permutations
import re

def palindromes_between_indices(s):
    s = ''.join(filter(str.isalpha, s[:7]))
    if not s:
        return set()
    s = s.lower()
    length = 7
    palindromes = set()
    while length <= len(s):
        for p in permutations(s, length):
            word = ''.join(p)
            if word == word[::-1]:
                palindromes.add(word)
        length += 1
    return palindromes