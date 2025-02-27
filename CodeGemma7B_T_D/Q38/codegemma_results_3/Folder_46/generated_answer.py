from itertools import combinations

def find_subset_of_length_n(set_x):
    return len(list(combinations(set_x, 14)))