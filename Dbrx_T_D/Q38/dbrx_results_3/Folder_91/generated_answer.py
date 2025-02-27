from itertools import combinations

def find_subset_of_length_n(elements):
    subsets = [subset for subset in combinations(elements, 6)]
    return len(subsets)