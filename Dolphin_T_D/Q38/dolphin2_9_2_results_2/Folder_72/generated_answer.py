def find_subset_of_length_n(s):
    if len(s) < 16:
        return 0
    subset_size = 16
    return len(s) - subset_size + 1