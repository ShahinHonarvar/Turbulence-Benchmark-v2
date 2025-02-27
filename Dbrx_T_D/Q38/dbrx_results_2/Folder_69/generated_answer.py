def find_subset_of_length_n(elements):
    if len(elements) < 894:
        return 0
    if len(elements) == 894:
        return 1 if set(elements) else 0
    return len(list(itertools.combinations(elements, 894)))