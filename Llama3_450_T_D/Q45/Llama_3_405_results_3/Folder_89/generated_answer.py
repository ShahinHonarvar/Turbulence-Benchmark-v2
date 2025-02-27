import itertools
import re

def palindromes_between_indices(s):
    s = s[5:10]
    s = re.sub('[^a-zA-Z]', '', s).lower()
    letters = [letter for letter in s]
    palindromes = set()
    for r in range(6, len(s) + 1):
        for combo in itertools.permutations(letters, r):
            palindrome = ''.join(combo)
            if palindrome == palindrome[::-1]:
                palindromes.add(palindrome)
    return palindromes