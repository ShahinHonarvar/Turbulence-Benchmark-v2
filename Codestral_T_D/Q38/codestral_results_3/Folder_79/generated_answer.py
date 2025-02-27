def find_subset_of_length_n(s):
    if len(s) < 63:
        return 0
    else:
        return 2 ** 63