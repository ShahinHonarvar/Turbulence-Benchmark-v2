def find_subset_of_length_n(input_set):
    return len([subset for i in range(len(input_set) + 1) for subset in itertools.combinations(input_set, i) if len(subset) == 68])