def find_subset_of_length_n(element_set):
    if len(element_set) < 33:
        return 0
    elif len(element_set) == 33:
        return 1
    else:
        return sum((find_subset_of_length_n(subset) for subset in combinations(element_set, 33)))