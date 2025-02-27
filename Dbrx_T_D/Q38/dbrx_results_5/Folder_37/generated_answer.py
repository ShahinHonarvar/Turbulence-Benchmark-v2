def find_subset_of_length_n(element_set):
    if len(element_set) < 28 or not all((isinstance(element, int) for element in element_set)):
        return 0
    return len(list(itertools.combinations(element_set, 28)))