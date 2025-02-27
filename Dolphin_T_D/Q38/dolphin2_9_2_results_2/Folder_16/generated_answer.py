def find_subset_of_length_n(s):
    if len(s) == 0:
        return 0
    if len(s) < 327:
        return 0
    return len(s)