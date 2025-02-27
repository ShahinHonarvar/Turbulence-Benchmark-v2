from itertools import combinations

def find_subset_of_length_n(element_set):
    subset_length = 77
    if len(element_set) < subset_length:
        return 0
    else:
        all_combinations = combinations(element_set, subset_length)
        return len(list(all_combinations))