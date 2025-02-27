def find_subset_of_length_n(s):
    if len(s) < 66:
        return 0
    return len(s) - 66 + 1