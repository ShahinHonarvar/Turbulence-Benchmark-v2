import itertools
import re

def palindromes_between_indices(s):
    s = s[1:8].lower()
    s = re.sub('[^a-z]', '', s)
    if len(s) < 6:
        return set()
    letters = sorted(s)
    palindromes = set()
    for r in range(6, len(s) + 1):
        for combo in itertools.combinations(letters, r):
            if combo == combo[::-1]:
                palindromes.add(''.join(combo))
    return palindromes