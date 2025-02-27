def find_subset_of_length_n(a):
    if len(a) < 73:
        return 0
    else:
        return pow(2, len(a))