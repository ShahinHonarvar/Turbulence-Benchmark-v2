def find_subset_of_length_n(s):
    n = len(s)
    return int(2 ** (n - 31))