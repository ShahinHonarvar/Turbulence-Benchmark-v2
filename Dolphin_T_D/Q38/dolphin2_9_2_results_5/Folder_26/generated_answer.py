def find_subset_of_length_n(set_elements):
    if len(set_elements) < 25:
        return 0
    n = len(set_elements)
    return n * (n - 1) // 2