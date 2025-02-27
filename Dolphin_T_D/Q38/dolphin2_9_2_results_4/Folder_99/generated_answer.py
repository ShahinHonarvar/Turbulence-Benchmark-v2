def find_subset_of_length_n(s):
    if len(s) < 307:
        return 0
    else:
        return len(s) * find_subset_of_length_n(s - 1)