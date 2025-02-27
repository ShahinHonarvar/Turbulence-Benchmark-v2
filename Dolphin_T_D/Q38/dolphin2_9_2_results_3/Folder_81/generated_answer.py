def find_subset_of_length_n(s):
    if not isinstance(s, set):
        s = set(s)
    n = 20
    return len([c for c in combinations(s, n)])