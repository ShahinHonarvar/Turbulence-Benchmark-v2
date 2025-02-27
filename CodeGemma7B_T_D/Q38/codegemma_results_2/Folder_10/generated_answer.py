from itertools import combinations

def find_subset_of_length_n(set_of_elements):
    return len([subset for subset in combinations(set_of_elements, 54)])