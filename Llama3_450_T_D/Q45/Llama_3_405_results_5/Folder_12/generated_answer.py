import itertools
from collections import Counter

def palindromes_between_indices(s):
    s = s[3:9].lower()
    s = ''.join(filter(str.isalpha, s))
    counter = Counter(s)
    palindromes = set()
    for r in range(4, len(s) + 1):
        for combo in itertools.combinations_with_replacement(counter.elements(), r):
            combo = ''.join(combo)
            if combo == combo[::-1]:
                palindromes.add(combo)
    return palindromes