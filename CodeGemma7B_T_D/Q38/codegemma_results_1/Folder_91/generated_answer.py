from itertools import combinations

def find_subset_of_length_n(num):
    return len(list(combinations(num, 6)))