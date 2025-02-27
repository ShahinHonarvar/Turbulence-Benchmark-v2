def find_subset_of_length_n(s):
    if len(s) < 80:
        return 0
    n = len(s)
    return n * find_subset_of_length_n(s - 1) + pow(-1, n) * find_subset_of_length_n(n - 1)