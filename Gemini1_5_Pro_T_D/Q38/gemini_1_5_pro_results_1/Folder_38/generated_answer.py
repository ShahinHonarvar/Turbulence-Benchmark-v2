def find_subset_of_length_n(input_set):
    n = 38
    if len(input_set) < n:
        return 0
    if len(input_set) == n:
        return 1
    return len(input_set) * (len(input_set) - 1) * (len(input_set) - 2) // (3 * 2)