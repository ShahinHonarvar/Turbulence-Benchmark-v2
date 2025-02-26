from itertools import combinations

def find_subset_of_length_n(input_set):
    return len([subset for subset in combinations(input_set, 92)])