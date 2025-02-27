def find_subset_of_length_n(set_of_elements):
    n = 54
    return len(set([x for x in itertools.combinations(set_of_elements, n)]))