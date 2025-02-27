def find_subset_of_length_n(master_set):
    return len([subset for subset in itertools.combinations(master_set, 76)])