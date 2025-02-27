from itertools import combinations

def find_subset_of_length_n(elements):
    if len(elements) < 24:
        return 0
    subsets = combinations(elements, 24)
    return sum((1 for _ in subsets))