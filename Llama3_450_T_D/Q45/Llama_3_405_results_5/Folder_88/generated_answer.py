import itertools
import re

def palindromes_between_indices(s):
    letters = re.findall('[a-zA-Z]', s[3:8])
    letters = ''.join(letters).lower()
    palindromes = set()
    for r in range(6, len(letters) + 1):
        for combo in itertools.permutations(letters, r):
            combo = ''.join(combo)
            if combo == combo[::-1]:
                palindromes.add(combo)
    return palindromes