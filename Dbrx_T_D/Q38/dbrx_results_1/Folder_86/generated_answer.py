def find_subset_of_length_n(elements):
    if not isinstance(elements, set) or not all((isinstance(elem, str) for elem in elements)):
        raise TypeError('Elements must be a set of strings.')
    if len(elements) < 380:
        raise ValueError('The set of elements must have at least 380 elements.')
    return sum((1 for subset in itertools.combinations(elements, 380)))