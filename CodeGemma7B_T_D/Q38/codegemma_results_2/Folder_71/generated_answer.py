from itertools import combinations

def find_subset_of_length_n(s, n):
    return len([c for c in combinations(s, n)])