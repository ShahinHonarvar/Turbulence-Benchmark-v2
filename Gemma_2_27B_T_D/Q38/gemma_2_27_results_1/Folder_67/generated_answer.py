def find_subset_of_length_n(elements):
    elements_list = list(elements)
    n = 43
    return len([subset for i in range(len(elements_list)) for subset in itertools.combinations(elements_list, n) if len(subset) == n])