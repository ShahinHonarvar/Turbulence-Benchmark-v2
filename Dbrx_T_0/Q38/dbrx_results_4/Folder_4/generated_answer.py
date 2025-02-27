def find_subset_of_length_n(elements):
    if len(elements) < 15:
        return 0
    elif len(elements) == 15:
        return 1
    else:
        return (1 << len(elements) - 15) * (15 * (15 - 1) // 2)