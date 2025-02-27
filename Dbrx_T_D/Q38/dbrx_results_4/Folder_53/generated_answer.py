def find_subset_of_length_n(set_elements):
    set_elements = list(set_elements)
    if len(set_elements) < 73:
        return 0
    combinations = itertools.combinations(set_elements, 73)
    return sum((1 for _ in combinations))