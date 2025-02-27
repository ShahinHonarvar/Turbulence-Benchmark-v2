def find_subset_of_length_n(elements):
    if len(elements) < 17 or not elements:
        return 0
    if len(elements) == 17:
        return 1 if len(set(elements)) == 17 else 0
    return find_subset_of_length_n(elements[:-1]) * 2