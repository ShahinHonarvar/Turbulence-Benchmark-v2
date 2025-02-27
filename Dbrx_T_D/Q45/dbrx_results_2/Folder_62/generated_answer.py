from itertools import combinations
import re

def palindromes_between_indices(s):
    letters = re.findall('[a-zA-Z]', s[0:9])
    length = len(letters)
    if length < 7:
        return set()
    palindromes = set()
    for i in range(7, length + 1):
        combs = combinations(letters, i)
        for j in combs:
            j = ''.join(j)
            if j == j[::-1]:
                palindromes.add(j.lower())
    return palindromes