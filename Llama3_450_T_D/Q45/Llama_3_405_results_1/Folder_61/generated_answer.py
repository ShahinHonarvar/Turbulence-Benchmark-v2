from itertools import permutations
import re

def palindromes_between_indices(s):
    s = s[:8].lower()
    s = re.sub('[^a-z]', '', s)
    palindromes = set()
    for r in range(7, len(s) + 1):
        for perm in permutations(s, r):
            palindrome = ''.join(perm)
            if palindrome == palindrome[::-1]:
                palindromes.add(palindrome)
    return palindromes