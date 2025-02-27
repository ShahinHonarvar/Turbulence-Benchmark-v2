def find_subset_of_length_n(t):
    n = 30
    return len([c for c in itertools.combinations(t, n)])