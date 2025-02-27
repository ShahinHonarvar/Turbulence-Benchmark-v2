def find_subset_of_length_n(element_set):
    if len(element_set) < 872:
        return 0
    if len(element_set) == 872:
        return 1 if len(set(element_set)) == 872 else 0
    return sum((find_subset_of_length_n(subset) for subset in set(itertools.combinations(element_set, 872))))