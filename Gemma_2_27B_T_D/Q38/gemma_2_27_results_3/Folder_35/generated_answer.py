def find_subset_of_length_n(elements):
    return len([subset for subset in [set(combination) for combination in itertools.combinations(elements, 300)] if len(subset) == 300])