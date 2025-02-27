import itertools
from collections import Counter

def palindromes_between_indices(s):
    s = s[7:10].lower()
    s = ''.join(filter(str.isalpha, s))
    counter = Counter(s)
    palindromes = set()
    for r in range(3, len(s) + 1):
        for combo in itertools.combinations_with_replacement(counter.elements(), r):
            combo_str = ''.join(combo)
            if combo_str == combo_str[::-1]:
                palindromes.add(combo_str)
    return palindromes