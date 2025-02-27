from itertools import combinations

def find_subset_of_length_n(elements):
    return len(list(combinations(elements, 77))) if len(elements) >= 77 else 0