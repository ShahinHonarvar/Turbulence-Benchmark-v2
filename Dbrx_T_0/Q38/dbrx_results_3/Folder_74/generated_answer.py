def find_subset_of_length_n(elements):
    if len(elements) < 48:
        return 0
    elif len(elements) == 48:
        return 1
    else:
        return sum((find_subset_of_length_n(subset) for subset in itertools.combinations(elements, 48)))