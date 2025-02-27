def find_subset_of_length_n(elements):
    if len(elements) < 99:
        return 0
    elif len(elements) == 99:
        return 1
    else:
        return (1 << len(elements) - 99) * (99 * (99 - 1) // 2)