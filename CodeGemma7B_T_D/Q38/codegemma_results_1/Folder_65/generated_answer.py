from itertools import combinations

def find_subset_of_length_n(test_set, n):
    res = list(combinations(test_set, n))
    return len(res)