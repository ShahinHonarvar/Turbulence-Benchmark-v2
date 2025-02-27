def find_subset_of_length_n(set_elements):
    if len(set_elements) < 63:
        return 0
    return len(list(itertools.combinations(set_elements, 63)))