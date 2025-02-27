def find_subset_of_length_n(set_of_elements):
    return len({tuple(sub) for sub in itertools.combinations(set_of_elements, 85)})