def find_subset_of_length_n(elements):
    n = 14
    return len([subset for subset in [set(itertools.combinations(elements, i)) for i in range(n + 1)][n]])