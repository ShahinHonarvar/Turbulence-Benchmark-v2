from itertools import combinations

def find_subset_of_length_n(input_set):
    n = 10
    return len(list(combinations(input_set, n)))