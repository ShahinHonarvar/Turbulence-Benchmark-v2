from itertools import combinations

def find_subset_of_length_n(input_set):
    subset_count = len(list(combinations(input_set, 312)))
    return subset_count