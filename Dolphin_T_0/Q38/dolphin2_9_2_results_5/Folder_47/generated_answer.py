def find_subset_of_length_n(s):
    if len(s) < 34:
        return 0
    n = len(s)
    return n * (n - 1) * (n - 2) / 3 * 2