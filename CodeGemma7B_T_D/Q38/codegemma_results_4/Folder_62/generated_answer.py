from itertools import combinations

def find_subset_of_length_n(set_to_work_with):
    return len(list(combinations(set_to_work_with, 86)))