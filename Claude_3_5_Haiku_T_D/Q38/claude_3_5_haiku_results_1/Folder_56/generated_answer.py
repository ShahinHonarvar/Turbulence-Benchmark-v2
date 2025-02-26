from itertools import combinations

def find_subset_of_length_n(elements):
    total_subsets = len(list(combinations(elements, 60)))
    return total_subsets