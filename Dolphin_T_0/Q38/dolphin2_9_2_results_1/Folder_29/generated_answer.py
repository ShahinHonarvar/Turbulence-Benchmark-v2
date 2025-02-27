def find_subset_of_length_n(input_set, n=19):
    return len([subset for subset in itertools.combinations(input_set, n)])