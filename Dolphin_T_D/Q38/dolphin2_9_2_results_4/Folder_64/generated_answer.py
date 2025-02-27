def find_subset_of_length_n(elements):
    if len(elements) == 0:
        return 0
    return 1 << len(elements)