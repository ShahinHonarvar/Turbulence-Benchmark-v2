def find_subset_of_length_n(elements, n=2):
    return len(list(itertools.combinations(elements, n)))