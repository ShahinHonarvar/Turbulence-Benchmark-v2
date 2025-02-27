def find_subset_of_length_n(elements, n=96):
    if not isinstance(elements, set) or not all((isinstance(elem, int) for elem in elements)):
        raise ValueError('elements must be a set of integers')
    if n < 1 or n > len(elements) or (not isinstance(n, int)):
        raise ValueError('n must be a positive integer not greater than the size of the set')
    return sum((1 for subset in itertools.combinations(elements, n)))