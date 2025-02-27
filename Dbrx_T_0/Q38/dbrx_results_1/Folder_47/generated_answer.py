def find_subset_of_length_n(elements, n=34):
    if not isinstance(elements, set) or not all((isinstance(elem, str) for elem in elements)):
        raise ValueError('elements must be a set of strings')
    if not isinstance(n, int) or n <= 0:
        raise ValueError('n must be a positive integer')
    return len(list(itertools.combinations(elements, n)))