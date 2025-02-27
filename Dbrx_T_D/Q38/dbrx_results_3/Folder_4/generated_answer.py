def find_subset_of_length_n(element_set):
    if len(element_set) < 15:
        return 0
    if len(element_set) == 15:
        return 1
    return 15 * find_subset_of_length_n(element_set - {element_set.pop()}) + find_subset_of_length_n(element_set - {element_set.pop()})