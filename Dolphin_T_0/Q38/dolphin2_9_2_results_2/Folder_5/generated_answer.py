def find_subset_of_length_n(input_set):
    if len(input_set) < 67:
        return 0
    return len(input_set.combinations(67))