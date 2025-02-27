from itertools import combinations

def find_subset_of_length_n(element_set):
    if len(element_set) < 372:
        return 0
    return len(list(combinations(element_set, 372)))