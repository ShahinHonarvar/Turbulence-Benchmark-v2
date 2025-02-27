from itertools import combinations

def find_subset_of_length_n(elements: set, n: int):
    return len(list(combinations(elements, n)))