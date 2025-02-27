import itertools
from collections import Counter

def palindromes_between_indices(s):
    letters = [c for c in s[4:10] if c.isalpha()]
    letters = ''.join(letters).lower()
    counter = Counter(letters)
    palindromes = set()
    for r in range(7, len(letters) + 1):
        for combo in itertools.combinations_with_replacement(counter.elements(), r):
            combo = ''.join(combo)
            if combo == combo[::-1]:
                palindromes.add(combo)
    return palindromes