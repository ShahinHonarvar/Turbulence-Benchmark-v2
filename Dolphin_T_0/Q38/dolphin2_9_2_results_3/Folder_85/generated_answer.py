def find_subset_of_length_n(s):
    if len(s) < 23:
        return 0
    n = len(s)
    return n * n - 1