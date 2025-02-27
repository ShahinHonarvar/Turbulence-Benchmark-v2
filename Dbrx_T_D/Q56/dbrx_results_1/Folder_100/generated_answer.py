from itertools import combinations

def all_substring_of_size_n(s):
    n = 92
    if len(s) < n or len(set(s)) < n:
        return []
    return [''.join(substr) for substr in combinations(s, n) if len(''.join(substr)) == n and len(set(substr)) == n]