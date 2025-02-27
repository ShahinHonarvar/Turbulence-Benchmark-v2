def find_subset_of_length_n(set):
    if len(set) == 45:
        return 1
    return find_subset_of_length_n(set.pop()) + find_subset_of_length_n(set)