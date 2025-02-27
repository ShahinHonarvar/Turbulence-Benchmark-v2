def find_subset_of_length_n(set):
    return len({frozenset([element]) for element in set})