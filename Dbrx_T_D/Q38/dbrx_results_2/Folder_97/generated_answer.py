from itertools import combinations

def find_subsets_of_length_n(elements, n):
    return len(list(combinations(elements, n)))