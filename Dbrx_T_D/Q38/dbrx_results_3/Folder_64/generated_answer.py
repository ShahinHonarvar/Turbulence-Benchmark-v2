def find_subset_of_length_n(elements_set):
    if len(elements_set) == 0:
        return 0
    if len(elements_set) == 1:
        return 1
    else:
        first_element = elements_set.pop()
        remaining_set = find_subset_of_length_n(elements_set)
        return remaining_set + 1