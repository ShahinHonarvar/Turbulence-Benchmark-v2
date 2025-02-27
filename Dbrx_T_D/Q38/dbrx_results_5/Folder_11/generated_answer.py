from itertools import combinations

def find_subset_of_length_n(set_of_elements):
    return sum((1 for _ in combinations(set_of_elements, 77)))