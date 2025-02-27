def find_subset_of_length_n(set_elements):
    if len(set_elements) < 77:
        return 0
    return len({subset for subset in combinations(set_elements, 77)})