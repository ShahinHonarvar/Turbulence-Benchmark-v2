from itertools import combinations

def find_subset_of_length_n(data):
    n = 47
    return sum((1 for subset in combinations(data, n) if len(subset) == n))