from itertools import permutations
from string import ascii_lowercase

def palindromes_between_indices(s):
    s = s[5:10].lower()
    letters = ''.join(filter(lambda x: x in ascii_lowercase, s))
    pals = set()
    for r in range(5, len(letters) + 1):
        for perm in permutations(letters, r):
            word = ''.join(perm)
            if word == word[::-1]:
                pals.add(word)
    return pals