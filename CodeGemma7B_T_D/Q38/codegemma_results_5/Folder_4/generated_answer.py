def find_subset_of_length_n(set):
    if len(set) == 0:
        return 0
    return 2 ** len(set)