from itertools import combinations

def find_subset_of_length_n(elements):
    return len(set(combinations(elements, 30)))