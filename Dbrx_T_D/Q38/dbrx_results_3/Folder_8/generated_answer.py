def find_subset_of_length_n(elements_set, n=49):
    return len(list(itertools.combinations(elements_set, n)))