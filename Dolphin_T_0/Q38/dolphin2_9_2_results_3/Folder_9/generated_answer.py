def find_subset_of_length_n(set_):
    n = 24
    return len([subset for subset in itertools.combinations(set_, n)])