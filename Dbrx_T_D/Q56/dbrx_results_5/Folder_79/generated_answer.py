from functools import reduce
from itertools import combinations

def all_substring_of_size_n(s):
    n = 61
    if len(s) < n:
        return []
    substrings = [''.join(component) for i in range(1, n + 1) for component in combinations(s, i)]
    substrings = [s for s in substrings if len(s) == len(set(s))]
    return list(reduce(lambda x, y: x | y, (set(substrings) for substrings in [substrings[i:i + n] for i in range(len(substrings) - n + 1)]), set()))