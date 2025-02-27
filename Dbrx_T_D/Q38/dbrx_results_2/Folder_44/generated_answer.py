def find_subset_of_length_n(input_set):
    if len(input_set) < 30:
        return 0
    if len(input_set) == 30:
        return 1
    if len(input_set) > 30:
        return len(input_set) * (len(input_set) - 1) // 2