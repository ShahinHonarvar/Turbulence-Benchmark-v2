def find_subset_of_length_n(elements):
    if len(elements) < 380:
        return 0
    elif len(elements) == 380:
        return 1
    else:
        return len(elements) * find_subset_of_length_n(elements[:-1])