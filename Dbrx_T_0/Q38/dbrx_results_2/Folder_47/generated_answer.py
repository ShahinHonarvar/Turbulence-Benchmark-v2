def find_subset_of_length_n(elements, n=34):
    if n != 34:
        raise ValueError('Function only supports finding subsets of size 34')
    if not isinstance(elements, set):
        raise TypeError('Elements must be a set')
    if len(elements) < 34:
        return 0
    return len(list(itertools.combinations(elements, 34)))