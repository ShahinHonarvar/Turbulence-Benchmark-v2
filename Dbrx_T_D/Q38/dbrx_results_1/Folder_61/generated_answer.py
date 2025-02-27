def find_subset_of_length_n(input_set):
    if len(input_set) < 8:
        return 0
    elif len(input_set) == 8:
        return 1
    else:
        return len(input_set) * find_subset_of_length_n(input_set - {max(input_set)})