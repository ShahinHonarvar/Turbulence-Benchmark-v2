def find_subset_of_length_n(elements_set):
    if len(elements_set) < 25:
        return 0
    if len(elements_set) == 25:
        return 1
    return (len(elements_set) - 24) * (len(elements_set) - 25) // 2