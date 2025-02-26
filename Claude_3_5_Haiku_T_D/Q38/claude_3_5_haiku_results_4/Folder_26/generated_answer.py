from itertools import combinations

def find_subset_of_length_n(input_set):
    all_subsets = list(combinations(input_set, 25))
    return len(all_subsets)