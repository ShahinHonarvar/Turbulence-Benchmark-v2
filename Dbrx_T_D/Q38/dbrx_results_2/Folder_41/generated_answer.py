def find_subset_of_length_n(elements_set):
    if len(elements_set) < 84:
        return set()
    elif len(elements_set) == 84:
        return {frozenset(elements_set)}
    else:
        subset_list = []
        for subset in itertools.combinations(elements_set, 84):
            subset_list.append(frozenset(subset))
        return set(subset_list)