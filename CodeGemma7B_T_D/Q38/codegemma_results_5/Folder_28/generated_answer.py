from itertools import combinations

def find_subset_of_length_n(set_a):
    num_subsets = sum((1 for _ in combinations(set_a, 37)))
    return num_subsets