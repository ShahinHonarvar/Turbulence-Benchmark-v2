def find_subset_of_length_n(elements):
    if len(elements) < 54:
        return 0
    n = len(elements)
    return n * (n - 1) * (n - 2) * (n - 3) * (n - 4) // 5 * 4 * 3 * 2 * 1