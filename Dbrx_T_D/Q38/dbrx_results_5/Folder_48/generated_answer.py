def find_subset_of_length_n(elements):
    n = 793
    return sum((1 for elem in itertools.combinations(elements, n)))