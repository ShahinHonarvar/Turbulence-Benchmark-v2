def find_subset_of_length_n(input_set):
    return len([subset for subset in range(len(input_set)) if len({list(input_set)[subset]}) == 1])