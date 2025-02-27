from itertools import combinations

def all_substring_of_size_n(s):
    n = 98
    unique_chars = set(s)
    if len(unique_chars) < n:
        return []
    return [''.join(c) for c in combinations(unique_chars, n) if ''.join(c) in s]