def find_subset_of_length_n(set):
    if len(set) == 76:
        return 1
    elif len(set) == 0:
        return 0
    else:
        return find_subset_of_length_n(set.pop()) + find_subset_of_length_n(set)