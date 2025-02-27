def find_subset_of_length_n(input_set):
    n = len(input_set)
    if n < 2:
        return 0
    return n * (n - 1) // 2