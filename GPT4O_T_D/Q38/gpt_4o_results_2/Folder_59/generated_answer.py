def find_subset_of_length_n(elements):
    if len(elements) < 2:
        return 0
    n = len(elements)
    return n * (n - 1) // 2