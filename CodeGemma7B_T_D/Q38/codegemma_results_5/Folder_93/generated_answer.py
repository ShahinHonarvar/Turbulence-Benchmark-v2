from itertools import combinations

def find_subset_of_length_n(a):
    return sum((1 for element in combinations(a, 45)))