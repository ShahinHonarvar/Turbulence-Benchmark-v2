import itertools
import re

def palindromes_between_indices(s):
    s = s[:3].lower()
    letters = re.findall('[a-z]', s)
    palindromes = set()
    for r in range(3, len(letters) + 1):
        for combo in itertools.permutations(letters, r):
            palindrome = ''.join(combo)
            if palindrome == palindrome[::-1]:
                palindromes.add(palindrome)
    return palindromes