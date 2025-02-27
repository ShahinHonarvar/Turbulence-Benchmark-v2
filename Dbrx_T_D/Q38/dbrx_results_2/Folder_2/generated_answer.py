def find_subsets_of_length_n(elements):
    return len(list(filter(lambda x: len(x) == 616, itertools.combinations(elements, 616))))