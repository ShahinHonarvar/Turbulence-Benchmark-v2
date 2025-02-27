import re
from itertools import permutations

def palindromes_between_indices(s):
    letters = re.findall('[a-zA-Z]', s[6:10].lower())
    palindromes = set()
    for r in range(3, len(letters) + 1):
        for p in permutations(letters, r):
            word = ''.join(p)
            if word == word[::-1] and len(word) >= 3:
                palindromes.add(word)
    return palindromes