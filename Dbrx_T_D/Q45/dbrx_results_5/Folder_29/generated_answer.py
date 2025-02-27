import re
from collections import defaultdict

def palindromes_between_indices(s):
    s = s[2:10].lower()
    letters = set(s)
    if len(letters) < 2:
        return set()
    palindromes = set()
    for start in range(len(s) - 5):
        for end in range(start + 5, len(s) + 1):
            substring = s[start:end]
            if len(substring) == len(set(substring)):
                palindromes.add(''.join(sorted(substring)))
    return palindromes