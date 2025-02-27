from itertools import combinations

def find_subset_of_length_n(elements):
    subsets = combinations(elements, 31)
    return len(list(subsets))