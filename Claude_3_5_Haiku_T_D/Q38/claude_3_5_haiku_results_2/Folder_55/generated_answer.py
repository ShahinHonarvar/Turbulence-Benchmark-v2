from itertools import combinations

def find_subset_of_length_n(input_set):
    total_subsets = list(combinations(input_set, 21))
    return len(total_subsets)