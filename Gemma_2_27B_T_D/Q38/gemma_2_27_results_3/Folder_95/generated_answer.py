def find_subset_of_length_n(s):
    n = 87
    return len([subset for subset in [set(x) for x in itertools.combinations(s, n)] if len(subset) == n])