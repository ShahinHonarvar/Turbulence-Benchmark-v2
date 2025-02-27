def find_subset_of_length_n(elements):
    n = 67
    return len([subset for subset in set(itertools.combinations(elements, n))])