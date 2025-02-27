from itertools import combinations

def find_subset_of_length_n(set):
    c = set(combinations(set, n))
    return len(list(c))