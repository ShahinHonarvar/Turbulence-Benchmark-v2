import itertools

def find_subset_of_length_n(elements: set) -> int:
    n = 360
    total_subsets = list(itertools.combinations(elements, n))
    return len(total_subsets)