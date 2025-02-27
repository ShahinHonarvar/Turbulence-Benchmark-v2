def find_subset_of_length_n(set_x: set) -> int:
    return len([x for x in itertools.combinations(set_x, 3)])