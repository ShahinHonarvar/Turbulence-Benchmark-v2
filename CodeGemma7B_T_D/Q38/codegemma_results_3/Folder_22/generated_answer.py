from itertools import combinations

def find_subset_of_length_n(s):
    n = 72
    return sum((1 for _ in combinations(s, n)))