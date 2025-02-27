def find_subset_of_length_n(num_set):
    return len([subset for subset in itertools.combinations(num_set, 7)])