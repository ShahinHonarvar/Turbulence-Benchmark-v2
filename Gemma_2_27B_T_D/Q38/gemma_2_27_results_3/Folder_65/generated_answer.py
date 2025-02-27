def find_subset_of_length_n(s):
    n = 35
    return len([subset for subset in itertools.combinations(s, n)])