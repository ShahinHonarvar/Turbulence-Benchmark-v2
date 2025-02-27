from itertools import combinations

def find_subset_of_length_n(n):
    return len(list(combinations(n, 40)))