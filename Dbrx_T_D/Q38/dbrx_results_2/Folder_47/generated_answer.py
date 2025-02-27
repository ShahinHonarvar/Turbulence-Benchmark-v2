def find_subset_of_length_n(element_set):
    if len(element_set) < 34:
        return 0
    if len(element_set) == 34:
        return 1
    return (len(element_set) - 33) * find_subset_of_length_n(element_set.difference(element_set[-1:]))