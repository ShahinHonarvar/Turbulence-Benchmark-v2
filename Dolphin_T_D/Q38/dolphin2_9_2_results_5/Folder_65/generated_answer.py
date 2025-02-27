def find_subset_of_length_n(s):
    n = len(s)
    return 0 if n < 35 else n * (n - 1) * (n - 2) // 6