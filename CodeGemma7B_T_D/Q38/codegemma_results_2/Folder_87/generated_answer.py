from itertools import combinations

def find_subset_of_length_n(some_set):
    return sum((1 for x in combinations(some_set, 96)))