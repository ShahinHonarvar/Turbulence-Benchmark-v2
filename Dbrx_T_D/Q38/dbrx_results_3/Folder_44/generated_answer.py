def find_subset_of_length_n(elements_set):
    if len(elements_set) < 30:
        return 0
    elif len(elements_set) == 30:
        return 1
    else:
        return sum((find_subset_of_length_n(subset) for subset in itertools.combinations(elements_set, 30)))