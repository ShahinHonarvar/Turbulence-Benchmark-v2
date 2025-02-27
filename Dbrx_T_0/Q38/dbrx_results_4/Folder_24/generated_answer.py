def find_subset_of_length_n(elements):
    if len(elements) < 74:
        return 0
    if len(elements) == 74:
        return 1
    return 2 ** (len(elements) - 74) * (74 * (74 - 1) // 2)