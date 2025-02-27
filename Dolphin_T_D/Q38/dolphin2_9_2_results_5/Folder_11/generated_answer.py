def find_subset_of_length_n(s):
    if len(s) < 77:
        return 0
    n = len(s) - 77
    return n * (n + 1) // 2