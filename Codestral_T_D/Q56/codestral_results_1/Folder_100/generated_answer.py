from itertools import combinations

def all_substring_of_size_n(s):
    return [''.join(sub) for sub in combinations(set(s), 92) if len(''.join(sub)) == 92]