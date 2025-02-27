def find_subset_of_length_n(element_set):
    return len({frozenset([i]) for i in element_set})