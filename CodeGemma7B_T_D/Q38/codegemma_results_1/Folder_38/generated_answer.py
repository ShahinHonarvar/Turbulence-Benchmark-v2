from itertools import combinations

def find_subset_of_length_n(subset):
    return len(list(combinations(subset, 38)))