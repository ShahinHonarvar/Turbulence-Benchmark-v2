def find_subset_of_length_n(elements, n=14):
    if n != 14:
        raise ValueError('Function only supports finding subsets of size 14')
    if not isinstance(elements, set):
        raise TypeError('Elements must be a set')
    if len(elements) < 14:
        return 0
    return len(list(itertools.combinations(elements, 14)))