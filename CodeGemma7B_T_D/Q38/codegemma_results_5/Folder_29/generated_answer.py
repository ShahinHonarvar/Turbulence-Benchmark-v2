from itertools import combinations

def find_subset_of_length_19(set):
    return len(list(combinations(set, 19)))