from itertools import combinations

def find_subset_of_length_n(my_set):
    result = list(combinations(my_set, n))
    return len(result)