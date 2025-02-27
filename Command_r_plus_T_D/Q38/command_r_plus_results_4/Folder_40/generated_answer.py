from itertools import combinations

def find_subset_of_length_n(elements: set) -> int:
    return len(list(combinations(elements, 7)))