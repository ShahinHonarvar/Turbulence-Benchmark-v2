def find_subset_of_length_n(s):
    if len(s) < 77:
        return 0
    return len(s) - 77 + 1