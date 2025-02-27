from itertools import combinations

def find_subset_of_length_n(elements):
    if len(elements) < 372:
        return 0
    return len(list(combinations(elements, 372)))