def find_subset_of_length_n(elements):
    return len([subset for subset in [set(x) for x in itertools.combinations(elements, 74)] if len(subset) == 74])