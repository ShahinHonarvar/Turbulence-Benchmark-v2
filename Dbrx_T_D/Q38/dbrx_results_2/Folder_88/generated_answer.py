def find_subsets_of_length_n(elements):
    if len(elements) < 46:
        raise ValueError('Set of elements must contain at least 46 elements')
    return len(list(itertools.combinations(elements, 46)))