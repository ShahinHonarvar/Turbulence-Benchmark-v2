from itertools import combinations

def find_subset_of_length_n(elements):
    subsets = list(combinations(elements, 56))
    return len(subsets)