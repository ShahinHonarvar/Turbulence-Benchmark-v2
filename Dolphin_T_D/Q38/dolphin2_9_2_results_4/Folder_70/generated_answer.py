def find_subset_of_length_n(s):
    if len(s) < 534:
        return 0
    n = len(s)
    return n - 534 + 1