from itertools import combinations

def find_subset_of_length_n(elements):
    return len(list(combinations(elements, 31))) if len(elements) >= 31 else 0