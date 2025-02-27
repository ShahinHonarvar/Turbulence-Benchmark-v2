import itertools
import re

def palindromes_between_indices(s):
    letters = re.findall('[a-zA-Z]', s[:8])
    letters = ''.join(letters).lower()
    palindromes = set()
    for r in range(7, len(letters) + 1):
        for combo in itertools.permutations(letters, r):
            palindrome = ''.join(combo)
            if palindrome == palindrome[::-1]:
                palindromes.add(palindrome)
    return palindromes