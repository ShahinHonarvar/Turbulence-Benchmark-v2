from itertools import combinations

def find_subset_of_length_n(elements):
    return sum((1 for _ in combinations(elements, 630)))