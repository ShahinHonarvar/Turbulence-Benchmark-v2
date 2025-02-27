from itertools import permutations
from string import ascii_lowercase, ascii_uppercase

def unique(p):
    return ''.join(sorted(p))

def palindromes_between_indices(s):
    length = 3
    palindrome_set = set()
    if len(s) < 9:
        return palindrome_set
    s = s[6:10].lower()
    for i in range(1, len(s)):
        for j in range(i + 1, len(s) + 1):
            if len(set(s[i:j])) < length:
                continue
            for p in permutations(s[i:j]):
                palindrome_set.add(unique(p))
    return palindrome_set