def find_subset_of_length_n(set):
    if len(set) == 0:
        return 1
    else:
        first_element = set.pop(0)
        without_first_element = find_subset_of_length_n(set)
        return without_first_element + len(set) * find_subset_of_length_n(set)