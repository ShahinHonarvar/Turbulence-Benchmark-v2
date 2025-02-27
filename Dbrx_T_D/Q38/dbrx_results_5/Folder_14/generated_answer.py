def find_subset_of_length_n(elements_set):
    if len(elements_set) < 17:
        return 0
    if len(elements_set) == 17:
        return 1 if len(set(elements_set)) == 17 else 0
    return sum((find_subset_of_length_n(subset) for subset in set(itertools.combinations(elements_set, 17))))