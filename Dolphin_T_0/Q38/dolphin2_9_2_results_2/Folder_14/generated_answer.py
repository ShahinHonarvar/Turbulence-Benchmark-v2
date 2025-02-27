def find_subset_of_length_n(s):
    if len(s) < 17:
        return 0
    elif len(s) == 17:
        return 1
    else:
        return len(s) * find_subset_of_length_n(s - 1)