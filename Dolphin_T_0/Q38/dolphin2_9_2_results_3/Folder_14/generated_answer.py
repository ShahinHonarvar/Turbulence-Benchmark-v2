def find_subset_of_length_n(s):
    return len([subset for subset in itertools.combinations(s, 17)])