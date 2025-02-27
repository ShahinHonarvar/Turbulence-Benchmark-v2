def find_subset_of_length_n(elements, n=10):
    if not isinstance(elements, set) or not all((isinstance(el, int) for el in elements)):
        raise ValueError('elements must be a set of integers')
    if not isinstance(n, int) or n < 1:
        raise ValueError('n must be a positive integer')
    if len(elements) < n:
        return 0
    return sum((1 for _ in itertools.combinations(elements, n)))