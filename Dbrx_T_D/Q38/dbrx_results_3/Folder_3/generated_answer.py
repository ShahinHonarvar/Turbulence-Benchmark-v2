def find_subset_of_length_n(elements):
    if len(elements) < 100:
        return 0
    if len(elements) == 100:
        return 1
    return 1 + find_subset_of_length_n(elements[:-1])