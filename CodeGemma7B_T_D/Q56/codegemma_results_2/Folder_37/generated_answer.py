from itertools import combinations

def all_substring_of_size_n(s):
    return list({''.join(p) for p in combinations(s, 65)})