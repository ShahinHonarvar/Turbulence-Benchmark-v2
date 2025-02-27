from itertools import combinations

def find_subset_of_length_n(set_):
    return len(list(combinations(set_, 100)))