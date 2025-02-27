def find_subset_of_length_n(elements):
    length = 28
    return len([subset for subset in itertools.combinations(elements, length)])