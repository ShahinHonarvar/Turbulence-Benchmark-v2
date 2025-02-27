def find_subset_of_length_n(elements):
    n = 18
    if len(elements) < n:
        return 0
    return len([subset for subset in itertools.combinations(elements, n)])