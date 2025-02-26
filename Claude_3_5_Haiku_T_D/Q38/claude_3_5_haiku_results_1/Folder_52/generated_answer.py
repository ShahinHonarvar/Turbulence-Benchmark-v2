from itertools import combinations

def find_subset_of_length_n(elements):
    all_subsets = list(combinations(elements, 32))
    return len(all_subsets)