def find_subset_of_length_n(input_set):
    n = 28
    return len([comb for comb in itertools.combinations(input_set, n)])