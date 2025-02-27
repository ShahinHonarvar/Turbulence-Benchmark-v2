def find_subset_of_length_n(elements, n=16):
    if n != 16:
        raise ValueError('Function only supports subsets of size 16')
    if not isinstance(elements, set):
        raise TypeError('Elements must be a set')
    if len(elements) < 16:
        return 0
    elif len(elements) == 16:
        return 1
    else:
        return sum((find_subset_of_length_n(elements - {element}, n=16) for element in elements))