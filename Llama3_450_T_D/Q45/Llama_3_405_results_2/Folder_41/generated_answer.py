from collections import Counter
from itertools import permutations

def palindromes_between_indices(s):
    english_letters = [c for c in s[2:4] if c.isalpha()]
    letters = ''.join(english_letters).lower()
    counter = Counter(letters)
    palindromes = set()
    for r in range(3, len(english_letters) + 1):
        for perm in permutations(letters, r):
            if perm == perm[::-1]:
                palindromes.add(''.join(perm))
    return palindromes