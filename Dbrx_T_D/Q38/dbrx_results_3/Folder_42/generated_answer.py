from itertools import combinations

def find_subsets_of_length_n(element_set):
    if len(element_set) < 31:
        return 0
    else:
        return len(list(combinations(element_set, 31)))