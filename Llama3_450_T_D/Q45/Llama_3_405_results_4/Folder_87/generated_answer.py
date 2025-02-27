import itertools
from collections import Counter

def palindromes_between_indices(s):
    s = s[3:10].lower()
    s = ''.join(filter(str.isalpha, s))
    counter = Counter(s)
    palindromes = set()
    for r in range(3, len(s) + 1):
        for combo in itertools.combinations(s, r):
            combo = ''.join(combo)
            if combo == combo[::-1]:
                palindromes.add(combo)
    for p in list(palindromes):
        p_counter = Counter(p)
        if all((p_counter[c] <= counter[c] for c in p_counter)):
            continue
        else:
            palindromes.remove(p)
    return palindromes