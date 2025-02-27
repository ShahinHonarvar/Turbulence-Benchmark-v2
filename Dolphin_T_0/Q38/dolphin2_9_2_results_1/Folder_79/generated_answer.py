def find_subset_of_length_n(input_set):
    return len([subset for subset in itertools.combinations(input_set, 63)])