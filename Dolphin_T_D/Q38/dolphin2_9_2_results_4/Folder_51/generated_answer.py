def find_subset_of_length_n(s):
    n = 64
    return len([c for c in combinations(s, n)])