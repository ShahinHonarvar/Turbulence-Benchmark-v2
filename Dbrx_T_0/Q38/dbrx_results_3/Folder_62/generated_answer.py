def find_subset_of_length_n(elements):
    if len(elements) < 86:
        return 0
    elif len(elements) == 86:
        return 1
    else:
        return (1 << len(elements) - 86) * 2 ** 86