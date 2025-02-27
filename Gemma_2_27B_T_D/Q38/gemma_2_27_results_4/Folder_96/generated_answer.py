def find_subset_of_length_n(elements):
    n = 47
    return len([subset for subset in [set(combination) for combination in itertools.combinations(elements, n)] if len(subset) == n])