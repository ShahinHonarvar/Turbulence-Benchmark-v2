from itertools import combinations

def find_subset_of_length_n(input_set):
    return sum((1 for _ in combinations(input_set, 64)))