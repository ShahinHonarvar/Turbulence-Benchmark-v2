def find_subset_of_length_n(elements):
    n = 801
    return len([comb for comb in itertools.combinations(elements, n)])