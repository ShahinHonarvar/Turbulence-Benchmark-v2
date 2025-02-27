def find_subset_of_length_n(elements):
    if len(elements) < 76:
        return 0
    elif len(elements) == 76:
        return 1
    else:
        return (len(elements) - 75) * find_subset_of_length_n(elements[:-1]) + find_subset_of_length_n(elements[:-1])