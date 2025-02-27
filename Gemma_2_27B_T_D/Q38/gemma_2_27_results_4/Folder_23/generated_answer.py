from itertools import combinations

def find_subset_of_length_n(elements):
    n = 69
    return len([subset for i in range(len(elements)) for subset in combinations(elements, i) if len(subset) == n])