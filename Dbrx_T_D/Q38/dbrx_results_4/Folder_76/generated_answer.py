def find_subset_of_length_n(element_set):
    if len(element_set) < 312:
        raise ValueError('Set size must be at least 312 for finding subsets of size 312.')
    if len(element_set) == 312:
        return {frozenset(element_set)}
    return {frozenset(subset) for subset_len in range(1, 312) for subset in itertools.combinations(element_set, subset_len)}