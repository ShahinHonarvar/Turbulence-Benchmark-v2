def find_subset_of_length_n(elements):
    if len(elements) < 30:
        return 0
    elif len(elements) == 30:
        return 1
    else:
        return (1 << len(elements) - 30) * (30 * (30 - 1) // 2)