def find_subset_of_length_n(element_set):
    if len(element_set) < 1:
        return 0
    elif len(element_set) == 1:
        return 1
    else:
        return 1 + find_subset_of_length_n(element_set[1:])