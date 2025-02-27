from collections import Counter
from itertools import combinations

def if_contains_anagrams(lst):
    count = 0
    for pair in combinations(lst, 2):
        pair = list(pair)
        pair[0] = Counter(pair[0].lower())
        pair[1] = Counter(pair[1].lower())
        pair[0] = {k: v for k, v in pair[0].items() if k.isalpha()}
        pair[1] = {k: v for k, v in pair[1].items() if k.isalpha()}
        pair[0] = {k: v for k, v in pair[0].items() if k in pair[1]}
        pair[1] = {k: v for k, v in pair[1].items() if k in pair[0]}
        if min(len(pair[0]), len(pair[1])) >= 3 and pair[0] == pair[1]:
            count += 1
            if count > 11:
                return False
    return count <= 11