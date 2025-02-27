from itertools import combinations

def find_subset_of_length_n(lst):
    no_of_subsets = len(list(combinations(lst, 860)))
    return no_of_subsets