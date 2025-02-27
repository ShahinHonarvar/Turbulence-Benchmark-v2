def find_subset_of_length_n(input_set):
    if len(input_set) < 99:
        return 0
    input_list = list(input_set)
    return len(list(combinations(input_list, 99)))