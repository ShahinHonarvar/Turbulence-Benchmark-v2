def find_subset_of_length_n(elements):
    return len(list(filter(lambda x: len(x) == 99, itertools.combinations(elements, 99))))