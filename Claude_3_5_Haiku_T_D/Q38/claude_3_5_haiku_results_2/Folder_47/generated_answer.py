from itertools import combinations

def find_subset_of_length_n(input_set):
    subsets = list(combinations(input_set, 34))
    return len(subsets)