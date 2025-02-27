def find_subset_of_length_n(element_set):
    if len(element_set) < 312:
        return set()
    subset_count = 0
    for subset in itertools.combinations(element_set, 312):
        subset_count += 1
    return subset_count