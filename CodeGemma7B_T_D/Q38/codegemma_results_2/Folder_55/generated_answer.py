from itertools import combinations

def find_subset_of_length_n(elements):
    subsets = set(combinations(elements, 21))
    return len(subsets)