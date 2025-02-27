import itertools

def find_subset_of_length_n(elements: set) -> int:
    return len(list(itertools.combinations(elements, 360)))