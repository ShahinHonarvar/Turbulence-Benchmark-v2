def find_subset_of_length_n(s):
    n = 534
    return len([subset for subset in itertools.combinations(s, n)])