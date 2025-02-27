def find_subset_of_length_n(set_of_elements):
    n = 42
    return len([s for s in itertools.combinations(set_of_elements, n)])