def find_subset_of_length_n(element_set, n=67):
    if n != 67:
        raise ValueError('Function only supports subsets of size 67')
    if not isinstance(element_set, set):
        raise TypeError('Argument must be a set')
    return len(list(itertools.combinations(element_set, n)))