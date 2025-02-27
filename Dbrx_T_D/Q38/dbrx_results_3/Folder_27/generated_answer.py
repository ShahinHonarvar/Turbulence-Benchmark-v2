def find_subset_of_length_n(elements_set, subsets_size):
    if not isinstance(elements_set, set):
        raise ValueError('elements_set argument must be a set')
    if not isinstance(subsets_size, int):
        raise ValueError('subsets_size argument must be an integer')
    if subsets_size < 1:
        raise ValueError('subsets_size argument must be greater than or equal to 1')
    subsets_count = 0
    for combination in itertools.combinations(elements_set, subsets_size):
        subsets_count += 1
    return subsets_count