def find_subset_of_length_n(set_of_elements):
    length = len(set_of_elements)
    return int(length ** 2 * (length + 1) / 6)