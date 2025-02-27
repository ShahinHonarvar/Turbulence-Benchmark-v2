from itertools import permutations
from string import ascii_lowercase

def palindromes_between_indices(s):
    s = s.lower()
    letters = [c for c in s[2:4] if c in ascii_lowercase]
    palindromes = set()
    for r in range(3, len(letters) + 1):
        for p in permutations(letters, r):
            word = ''.join(p)
            if word == word[::-1]:
                palindromes.add(word)
    return palindromes