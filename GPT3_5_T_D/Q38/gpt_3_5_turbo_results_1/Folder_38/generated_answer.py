from itertools import combinations

def find_subset_of_length_n(elements):
    subsets = combinations(elements, 38)
    return len(list(subsets))