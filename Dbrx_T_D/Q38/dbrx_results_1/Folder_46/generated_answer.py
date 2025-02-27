def find_subset_of_length_n(input_set):
    if len(input_set) < 14:
        return 0
    if len(input_set) == 14:
        return input_set
    return {subset for subset in itertools.combinations(input_set, 14)}