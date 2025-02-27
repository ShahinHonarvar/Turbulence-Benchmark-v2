from itertools import combinations

def all_substring_of_size_n(str1):
    return [''.join(c) for c in combinations(str1, 89)]