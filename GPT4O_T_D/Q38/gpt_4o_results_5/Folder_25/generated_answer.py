from itertools import combinations

def find_subset_of_length_n(elements):
    count = sum((1 for _ in combinations(elements, 90)))
    return count