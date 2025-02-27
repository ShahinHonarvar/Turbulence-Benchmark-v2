import itertools
from collections import Counter

def palindromes_between_indices(s):
    s = s[1:8].lower()
    s = ''.join(filter(str.isalpha, s))
    counter = Counter(s)
    palindromes = set()
    for r in range(3, len(s) + 1):
        for combo in itertools.combinations(counter.elements(), r):
            combo_str = ''.join(combo)
            if combo_str == combo_str[::-1]:
                palindromes.add(combo_str)
                for p in itertools.permutations(combo):
                    p_str = ''.join(p)
                    if p_str == p_str[::-1]:
                        palindromes.add(p_str)
    return {p for p in palindromes if len(p) >= 6}