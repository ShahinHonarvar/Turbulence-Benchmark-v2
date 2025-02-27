from itertools import combinations

def find_subset_of_length_n(elements: set):
    return len(list(combinations(elements, 99)))