def find_subset_of_length_n(elements):
    if not isinstance(elements, set):
        raise TypeError('The elements argument must be a set')
    if len(elements) < 7:
        return 0
    subsets = itertools.combinations(elements, 7)
    return len(list(subsets))