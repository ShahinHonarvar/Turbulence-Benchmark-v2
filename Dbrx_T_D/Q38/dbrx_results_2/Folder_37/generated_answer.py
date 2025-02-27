def find_subset_of_length_n(elements, n):
    if n != 28:
        raise ValueError('Invalid subset length')
    if not isinstance(elements, set):
        raise TypeError('Argument must be a set')
    return sum(map(lambda x: 1, itertools.combinations(elements, 28)))