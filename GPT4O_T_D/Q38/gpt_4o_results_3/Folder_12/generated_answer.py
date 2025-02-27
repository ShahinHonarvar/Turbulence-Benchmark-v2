from itertools import combinations

def find_subset_of_length_n(elements_set):
    return len(list(combinations(elements_set, 27))) if len(elements_set) >= 27 else 0