def find_subset_of_length_n(set):
    if len(set) == 42:
        return 1
    else:
        return find_subset_of_length_n(set.pop()) + find_subset_of_length_n(set)