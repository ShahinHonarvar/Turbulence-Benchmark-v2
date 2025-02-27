def find_subset_of_length_n(elements):
    if not elements:
        return 0
    if len(elements) == 66:
        return 1
    subset_without_first = find_subset_of_length_n(elements[1:])
    subset_with_first = find_subset_of_length_n(elements[1:]) if elements[0] not in elements[1:] else 0
    return subset_without_first + subset_with_first