def find_subset_of_length_n(elements):
    if len(elements) < 64:
        return 0
    n = len(elements)
    return n * (n - 1) * (n - 2) * (n - 3) * (n - 4) * (n - 5) * (n - 6) * (n - 7)