def find_subset_of_length_n(elements_set):
    if len(elements_set) < 33:
        return 0
    subset_count = 0
    for element in elements_set:
        if len(elements_set) == 33:
            subset_count += 1
        elements_set.remove(element)
        subset_count += find_subset_of_length_n(elements_set)
    return subset_count