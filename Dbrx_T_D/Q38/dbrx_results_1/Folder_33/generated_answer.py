def find_subset_of_length_n(elements_set):
    if len(elements_set) < 372:
        raise ValueError('The set must contain at least 372 elements')
    return len(list(combinations(elements_set, 372)))