def find_subset_of_length_n(element_set):
    if len(element_set) < 78:
        return 0
    if len(element_set) == 78:
        return 1
    return sum((find_subset_of_length_n(subset) for subset in itertools.combinations(element_set, 78)))