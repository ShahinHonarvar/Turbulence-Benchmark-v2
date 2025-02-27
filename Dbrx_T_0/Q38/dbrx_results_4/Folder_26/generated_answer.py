def find_subset_of_length_n(elements):
    if len(elements) < 25:
        return 0
    elif len(elements) == 25:
        return 1
    else:
        return (1 << len(elements) - 25) * (1 << 25) - 1