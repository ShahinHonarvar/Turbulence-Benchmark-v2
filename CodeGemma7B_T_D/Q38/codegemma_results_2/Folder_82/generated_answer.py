from itertools import combinations

def find_subset_of_length_n(s):
    return sum((1 for subset in combinations(s, 83) for _ in subset))