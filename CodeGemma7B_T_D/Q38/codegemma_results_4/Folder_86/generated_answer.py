from itertools import combinations

def find_subset_of_length_n(num_set):
    return sum((1 for subset in combinations(num_set, 380)))