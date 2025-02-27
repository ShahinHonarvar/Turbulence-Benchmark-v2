from itertools import combinations

def find_subsets_of_length_n(s):
    num_subsets = 0
    for subset in combinations(s, n):
        num_subsets += 1
    return num_subsets