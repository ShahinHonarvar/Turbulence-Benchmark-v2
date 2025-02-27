def find_subset_of_length_n(elements):
    return len([set for set in itertools.combinations(elements, 25)])