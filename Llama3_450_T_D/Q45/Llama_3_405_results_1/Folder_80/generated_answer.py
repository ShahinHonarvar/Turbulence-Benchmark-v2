import itertools
import re

def palindromes_between_indices(s):
    english_letters = re.findall('[a-zA-Z]', s[3:9])
    letters = ''.join(english_letters).lower()
    palindromes = set()
    for r in range(7, len(letters) + 1):
        for perm in itertools.permutations(letters, r):
            p = ''.join(perm)
            if p == p[::-1]:
                palindromes.add(p)
    return palindromes