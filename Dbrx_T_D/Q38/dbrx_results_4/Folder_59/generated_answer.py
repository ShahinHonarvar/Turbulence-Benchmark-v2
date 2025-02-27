def find_subset_of_length_n(element_set):
    return sum((1 for subset in itertools.combinations(element_set, 2)))