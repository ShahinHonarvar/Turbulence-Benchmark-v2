def find_subset_of_length_n(elements):
    if len(elements) < 16:
        return 0
    elif len(elements) == 16:
        return 1
    else:
        return sum((find_subset_of_length_n(subset) for subset in itertools.combinations(elements, 16)))