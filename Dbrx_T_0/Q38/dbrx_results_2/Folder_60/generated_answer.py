def find_subset_of_length_n(elements, n):
    if n != 88:
        raise ValueError('Function only supports finding subsets of size 88')
    if not isinstance(elements, set):
        raise TypeError('Argument must be a set')
    if len(elements) < 88:
        return 0
    return len(list(itertools.combinations(elements, 88)))