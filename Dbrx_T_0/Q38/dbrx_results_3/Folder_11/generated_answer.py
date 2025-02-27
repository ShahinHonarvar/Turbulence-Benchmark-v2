def find_subset_of_length_n(elements):
    if len(elements) < 77:
        return 0
    if len(elements) == 77:
        return 1
    return (1 << len(elements) - 77) * (77 * (77 - 1) // 2)