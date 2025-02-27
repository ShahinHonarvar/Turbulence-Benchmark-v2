def find_subset_of_length_n(element_set):
    if len(element_set) < 72:
        return {}
    elif len(element_set) == 72:
        return {frozenset(element_set)}
    else:
        subset_count = 0
        for i in range(len(element_set) - 71, -1, -1):
            subset_count += find_subset_of_length_n(element_set - set(list(element_set)[i:i + 72]))
        return subset_count