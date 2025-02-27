from itertools import combinations

def find_subset_of_length_n(x):
    return len(list(combinations(x, 25)))