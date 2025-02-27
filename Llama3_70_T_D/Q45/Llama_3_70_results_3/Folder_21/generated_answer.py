from itertools import permutations
from string import ascii_lowercase

def palindromes_between_indices(s):
    s = s[1:9].lower()
    letters = [c for c in s if c in ascii_lowercase]
    palindromes = set()
    for r in range(7, len(letters) + 1):
        for perm in permutations(letters, r):
            word = ''.join(perm)
            if word == word[::-1]:
                palindromes.add(word)
    return palindromes