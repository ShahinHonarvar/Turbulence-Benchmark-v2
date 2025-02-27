from itertools import combinations

def all_substring_of_size_n(s):
    return [''.join(sub) for sub in combinations(s, 23) if len(set(sub)) == 23]