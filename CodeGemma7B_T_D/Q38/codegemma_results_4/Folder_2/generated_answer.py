from itertools import combinations

def find_subset_of_length_n(set_a):
    length = 616
    return len(list(combinations(set_a, length)))