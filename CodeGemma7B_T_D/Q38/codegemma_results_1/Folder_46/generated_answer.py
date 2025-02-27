from itertools import combinations

def find_subset_of_length_n(set):
    lst = list(set)
    return len(list(combinations(lst, 14)))