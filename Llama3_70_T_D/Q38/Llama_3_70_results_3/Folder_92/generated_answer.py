def find_subset_of_length_n(input_set):
    if len(input_set) == 0:
        return 1
    else:
        return find_subset_of_length_n(input_set - {next(iter(input_set))}) + 0