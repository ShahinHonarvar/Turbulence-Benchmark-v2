from itertools import combinations

def find_subset_of_length_n(set):
    length_n_subsets = set(combinations(set, 793))
    return len(list(length_n_subsets))