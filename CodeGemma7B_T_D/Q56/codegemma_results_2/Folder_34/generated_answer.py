from itertools import combinations_with_replacement

def all_substring_of_size_n(s):
    return sorted({''.join(comb) for comb in combinations_with_replacement(s, 84)})