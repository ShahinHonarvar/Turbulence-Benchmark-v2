from itertools import combinations

def find_subset_of_length_n(set):
    a = list(combinations(set, 24))
    return len(a)