def find_subset_of_length_n(elements: set, n: int=49):
    return len([comb for comb in combinations(elements, n)])