def find_subset_of_length_n(s):
    if len(s) < 96:
        return 0
    elif len(s) == 96:
        return 1
    else:
        return len(s) * find_subset_of_length_n(s - 1)