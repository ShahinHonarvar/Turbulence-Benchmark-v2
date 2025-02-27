def find_subset_of_length_n(elements, n=35):
    if n != 35:
        raise ValueError('Function only supports finding subsets of size 35')
    if not isinstance(elements, set):
        raise TypeError('Argument must be a set')
    if len(elements) < 35:
        return 0
    return len(list(itertools.combinations(elements, 35)))