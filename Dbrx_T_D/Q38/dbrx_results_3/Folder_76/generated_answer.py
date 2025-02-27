from itertools import combinations

def find_subset_of_length_n(elements_set, n):
    return len(list(combinations(elements_set, n)))