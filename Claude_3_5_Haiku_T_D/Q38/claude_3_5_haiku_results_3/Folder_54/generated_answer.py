from itertools import combinations

def find_subset_of_length_n(input_set):
    total_subsets = len(list(combinations(input_set, 51)))
    return total_subsets