from itertools import combinations

def find_subset_of_length_n(elements_set):
    length_of_subset = 88
    return len(list(combinations(elements_set, length_of_subset)))