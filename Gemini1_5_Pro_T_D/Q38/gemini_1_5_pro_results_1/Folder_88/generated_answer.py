def find_subset_of_length_n(set_of_elements):
    n = 46
    number_of_subsets = 0
    if len(set_of_elements) < n:
        return number_of_subsets
    else:
        for subset in itertools.combinations(set_of_elements, n):
            number_of_subsets += 1
    return number_of_subsets