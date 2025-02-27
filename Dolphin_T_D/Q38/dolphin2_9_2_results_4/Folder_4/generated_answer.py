from itertools import combinations

def find_subset_of_length_n(s):
    length_n_subsets = combinations(s, 15)
    return len(list(length_n_subsets))