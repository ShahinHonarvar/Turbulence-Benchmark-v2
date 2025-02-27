def find_subset_of_length_n(set):
    if len(set) == 0:
        return 1
    return len(set) * find_subset_of_length_n(set[1:])