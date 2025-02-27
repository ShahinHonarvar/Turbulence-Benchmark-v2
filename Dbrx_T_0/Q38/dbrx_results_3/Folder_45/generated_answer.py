def find_subset_of_length_n(elements, n):
    if n != 33:
        raise ValueError('Function only supports subsets of size 33')
    if not isinstance(elements, set):
        raise TypeError('Elements must be a set')
    if len(elements) < 33:
        return 0
    return len(list(itertools.combinations(elements, 33)))