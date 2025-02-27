from itertools import combinations

def find_subset_of_length_n(elements):
    n = 534
    return len(list(combinations(elements, n)))