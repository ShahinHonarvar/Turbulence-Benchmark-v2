def find_subsets_of_length_n(element_set):
    if len(element_set) < 22:
        return 0
    return len(list(itertools.combinations(element_set, 22)))