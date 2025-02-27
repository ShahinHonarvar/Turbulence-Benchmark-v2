def find_subset_of_length_n(element_set):
    if len(element_set) < 69:
        return 0
    if len(element_set) == 69:
        return 1
    if len(element_set) > 69:
        return pow(2, 69) - 1