def find_subset_of_length_n(element_set):
    if len(element_set) < 13 or not isinstance(element_set, set):
        return 0
    else:
        return sum((1 for _ in combinations(element_set, 13)))