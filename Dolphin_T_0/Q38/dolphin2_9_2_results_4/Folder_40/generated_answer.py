def find_subset_of_length_n(elements):
    return len(list(filter(lambda x: len(x) == 7, itertools.combinations(elements, 7))))