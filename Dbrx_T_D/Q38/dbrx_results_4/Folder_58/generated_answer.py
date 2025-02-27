def find_subsets_of_length_n(elements):
    return len(list(filter(lambda subset: len(subset) == 860, itertools.combinations(elements, 860))))