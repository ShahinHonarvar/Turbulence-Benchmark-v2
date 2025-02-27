from itertools import combinations

def find_subset_of_length_n(s):
    return sum((1 for c in combinations(s, 20)))