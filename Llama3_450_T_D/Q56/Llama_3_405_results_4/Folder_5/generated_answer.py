from itertools import combinations

def all_substring_of_size_n(s):
    return [''.join(x) for x in set(combinations(s, 64)) if len(set(x)) == 64]