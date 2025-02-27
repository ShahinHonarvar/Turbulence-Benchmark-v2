from itertools import combinations

def all_substring_of_size_n(s):
    if len(s) < 86 or len(set(s)) != 86:
        return []
    else:
        return [''.join(substr) for substr in combinations(s, 86)]