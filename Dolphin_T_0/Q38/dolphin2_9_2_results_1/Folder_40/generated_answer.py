def find_subset_of_length_n(elements: set) -> int:
    return len([x for x in elements.combinations(7)])