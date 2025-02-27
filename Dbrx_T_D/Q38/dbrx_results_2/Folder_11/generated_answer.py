from itertools import combinations

def find_subset_of_length_n(elements):
    if len(elements) < 77:
        return 0
    if len(elements) == 77:
        return 1
    if len(elements) > 77:
        return len(list(combinations(elements, 77)))