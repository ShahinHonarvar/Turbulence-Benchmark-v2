def find_subset_of_length_n(elements):
    if len(elements) < 99:
        raise ValueError('The set of elements should have at least 99 elements.')
    return len(list(itertools.combinations(elements, 99)))