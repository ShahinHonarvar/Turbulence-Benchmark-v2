def find_subset_of_length_n(s):
    n = len(s)
    if n < 83:
        return 0
    return n * (n - 1) * (n - 2) // 6