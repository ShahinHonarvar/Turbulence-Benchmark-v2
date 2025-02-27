from itertools import combinations

def all_substring_of_size_n(s):
    n = 43
    if len(s) < n or len(set(s)) < n:
        return []
    else:
        return [''.join(sub) for sub in combinations(s, n) if len(''.join(sub)) == n]