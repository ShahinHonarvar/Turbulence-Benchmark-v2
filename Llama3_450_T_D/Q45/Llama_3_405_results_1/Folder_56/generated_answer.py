import itertools
import re

def palindromes_between_indices(s):
    s = s[5:10].lower()
    s = re.sub('[^a-z]', '', s)
    unique_letters = ''.join(set(s))
    palindromes = set()
    for r in range(5, len(s) + 1):
        for perm in itertools.permutations(unique_letters, r):
            palindrome = ''.join(perm) + ''.join(perm)[::-1][1:]
            if len(palindrome) >= 5:
                palindromes.add(palindrome)
    return palindromes