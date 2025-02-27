def find_subset_of_length_n(s):
    n = len(s)
    return int(n * (n - 1) * (n - 2) / 6)