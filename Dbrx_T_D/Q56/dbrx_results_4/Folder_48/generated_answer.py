from itertools import combinations

def all_substring_of_size_n(s):
    n = 120
    if len(s) < n or len(set(s)) < n:
        return []
    else:
        return [''.join(substr) for substr in combinations(s, n) if len(set(substr)) == n]