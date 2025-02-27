def find_subset_of_length_n(elements):
    n = 85
    num_of_subsets = len(list(itertools.combinations(elements, n)))
    return num_of_subsets