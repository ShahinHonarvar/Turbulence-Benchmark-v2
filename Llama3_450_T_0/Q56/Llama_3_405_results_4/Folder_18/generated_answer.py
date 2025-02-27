from itertools import combinations

def all_substring_of_size_n(s):
    return [''.join(c) for c in combinations(set(s), 63) if ''.join(c) in s]