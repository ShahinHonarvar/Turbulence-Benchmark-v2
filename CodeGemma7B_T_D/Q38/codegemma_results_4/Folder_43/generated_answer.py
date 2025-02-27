def find_subset_of_length_n(set):
    if len(set) == 29:
        return 1
    else:
        return find_subset_of_length_n(set) + find_subset_of_length_n(set) - 1