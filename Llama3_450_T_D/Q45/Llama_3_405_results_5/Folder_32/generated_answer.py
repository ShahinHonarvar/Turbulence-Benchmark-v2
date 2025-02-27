import itertools
import re

def palindromes_between_indices(s):
    s = s[1:8].lower()
    s = ''.join((c for c in s if c.isalpha()))
    palindromes = set()
    for r in range(5, len(s) + 1):
        for perm in itertools.permutations(s, r):
            palindrome = ''.join(perm)
            if palindrome == palindrome[::-1]:
                palindromes.add(palindrome)
    return palindromes