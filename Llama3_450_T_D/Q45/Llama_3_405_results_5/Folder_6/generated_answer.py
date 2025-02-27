import itertools
from collections import Counter

def palindromes_between_indices(s):
    chars = [c.lower() for c in s[:8] if c.isalpha()]
    counter = Counter(chars)
    palindromes = set()
    for r in range(2, len(chars) + 1):
        for perm in itertools.permutations(chars, r):
            palindrome = ''.join(perm)
            if len(palindrome) >= 4 and palindrome == palindrome[::-1]:
                palindromes.add(palindrome)
    return palindromes