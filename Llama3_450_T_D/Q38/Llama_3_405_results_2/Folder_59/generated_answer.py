def find_subset_of_length_n(element_set):
    return len({frozenset([x, y]) for x in element_set for y in element_set if x != y}) // 2