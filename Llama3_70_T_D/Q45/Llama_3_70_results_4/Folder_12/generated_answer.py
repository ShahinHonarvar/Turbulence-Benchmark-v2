from itertools import permutations
from string import ascii_letters

def palindromes_between_indices(s):
    letters = [c for c in s[3:9].lower() if c in ascii_letters]
    palindromes = set()
    for r in range(4, len(letters) + 1):
        for p in permutations(letters, r):
            word = ''.join(p)
            if word == word[::-1]:
                palindromes.add(word)
    return palindromes