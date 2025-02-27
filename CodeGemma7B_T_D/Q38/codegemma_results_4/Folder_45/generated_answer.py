from itertools import combinations

def find_subset_of_length_n(input_set, n):
    return len(list(combinations(input_set, n)))