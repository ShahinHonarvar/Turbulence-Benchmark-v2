from itertools import combinations

def find_subset_of_length_n(my_set: set) -> int:
    return len(list(combinations(my_set, 180)))