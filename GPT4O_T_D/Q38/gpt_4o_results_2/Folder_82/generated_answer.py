from itertools import combinations

def find_subset_of_length_n(elements):
    if len(elements) < 83:
        return 0
    return len(list(combinations(elements, 83)))