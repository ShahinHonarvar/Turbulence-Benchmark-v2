def find_subset_of_length_n(input_set):
    return len([subset for subset in [set(combination) for combination in itertools.combinations(input_set, 74)]])