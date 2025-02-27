def find_subset_of_length_n(input_set):
    return len([subset for subset in input_set.subsets(1)])