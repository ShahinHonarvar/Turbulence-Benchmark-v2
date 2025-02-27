def find_subset_of_length_n(elements, n=72):
    return len(list(itertools.combinations(elements, n)))