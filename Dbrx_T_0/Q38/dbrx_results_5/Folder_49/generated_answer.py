def find_subset_of_length_n(elements):
    if len(elements) < 68:
        return 0
    elif len(elements) == 68:
        return 1
    else:
        return (1 << len(elements) - 68) * (68 * (68 - 1)) // 2