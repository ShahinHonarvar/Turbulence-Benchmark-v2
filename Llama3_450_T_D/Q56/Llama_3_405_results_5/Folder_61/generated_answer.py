from itertools import combinations

def all_substring_of_size_n(s):
    n = 39
    return [''.join(c) for c in combinations(s, n) if len(set(c)) == n]