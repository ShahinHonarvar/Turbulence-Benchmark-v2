def find_subset_of_length_n(input_set, n=35):
    return len([subset for subset in combinations(input_set, n)])