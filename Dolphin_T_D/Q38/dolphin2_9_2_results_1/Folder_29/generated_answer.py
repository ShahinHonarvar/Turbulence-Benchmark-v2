def find_subset_of_length_n(set_elements):
    return len([s for s in itertools.combinations(set_elements, 19)])