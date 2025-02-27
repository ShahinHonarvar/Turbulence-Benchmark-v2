from itertools import combinations

def find_subset_of_length_n(a):
    return len([list(c) for c in combinations(a, 68)])