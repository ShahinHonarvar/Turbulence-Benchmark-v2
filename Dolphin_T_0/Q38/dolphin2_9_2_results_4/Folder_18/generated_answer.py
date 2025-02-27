def find_subset_of_length_n(s):
    if len(s) < 630:
        return 0
    else:
        return pow(2, len(s) - 630)