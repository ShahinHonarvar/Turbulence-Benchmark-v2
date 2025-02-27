def find_subset_of_length_n(set_of_elements):
    n = 27
    if len(set_of_elements) < n:
        return 0
    elif len(set_of_elements) == n:
        return 1
    else:
        return len(set_of_elements) * (len(set_of_elements) - 1) // (27 * 26)