def find_subset_of_length_n(s):
    if not s:
        return 0
    n = len(s)
    return n * find_subset_of_length_n(s - 1) // (n - 23)