from itertools import combinations

def all_substring_of_size_n(s):
    return list({''.join(comb) for comb in combinations(s, 40)})