from itertools import combinations

def find_subset_of_length_n(set):
    return sum((1 for _ in combinations(set, n) if n == 894))