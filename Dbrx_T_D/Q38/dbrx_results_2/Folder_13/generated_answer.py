from itertools import combinations

def find_subsets_of_length_n(elements):
    return len(list(combinations(elements, 801)))