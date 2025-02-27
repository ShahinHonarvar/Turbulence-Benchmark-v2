def find_subset_of_length_n(set):
    if len(set) == 0:
        return 1
    return find_subset_of_length_n(set[1:]) + find_subset_of_length_n(set[:-1])