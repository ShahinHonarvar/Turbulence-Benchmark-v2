def find_subset_of_length_n(element_set):
    if not isinstance(element_set, set) or len(element_set) < 56:
        return None
    else:
        return sum((1 for subset in itertools.combinations(element_set, 56)))