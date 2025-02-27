from itertools import combinations

def find_subset_of_length_n(set, n):
    return len(list(combinations(set, n)))