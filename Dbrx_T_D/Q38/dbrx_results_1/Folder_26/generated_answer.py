def find_subset_of_length_n(input_set):
    if len(input_set) < 25:
        return 0
    elif len(input_set) == 25:
        return 1
    else:
        return (len(input_set) - 24) * find_subset_of_length_n(input_set - {min(input_set)})