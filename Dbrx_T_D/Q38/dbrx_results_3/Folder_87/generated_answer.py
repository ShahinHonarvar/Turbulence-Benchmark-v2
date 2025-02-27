from itertools import combinations

def find_subset_of_length_n(element_set):
    if len(element_set) < 96:
        return 0
    else:
        return len(list(combinations(element_set, 96)))