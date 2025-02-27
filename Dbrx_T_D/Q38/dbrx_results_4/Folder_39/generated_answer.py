def find_subset_of_length_n(elements):
    if len(elements) < 59:
        return 0
    if len(elements) == 59:
        return 1
    return sum((find_subset_of_length_n(subset) == 1 for subset in itertools.combinations(elements, 59)))