def find_subset_of_length_n(elements):
    n = 35
    return len([comb for comb in combinations(elements, n)])