from itertools import combinations

def all_substring_of_size_n(str):
    n = 93
    return [''.join(x) for x in combinations(str, n)]