def find_subset_of_length_n(elements_set):
    if len(elements_set) < 894:
        return 0
    else:
        return len(list(itertools.combinations(elements_set, 894)))