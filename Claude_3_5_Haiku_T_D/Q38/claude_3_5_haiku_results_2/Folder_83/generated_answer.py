from itertools import combinations

def find_subset_of_length_n(input_set):
    n = 95
    return sum((1 for _ in combinations(input_set, n)))