def find_subset_of_length_n(elements):
    n = 99
    return len([subset for subset in itertools.combinations(elements, n)])