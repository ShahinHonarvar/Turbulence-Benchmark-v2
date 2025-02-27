from itertools import combinations

def find_subset_of_length_n(element_set):
    n = 616
    return len(list(combinations(element_set, n)))