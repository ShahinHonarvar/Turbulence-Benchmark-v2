def find_subset_of_length_n(elements):
    n = 91
    if n > len(elements):
        return 0
    return len([subset for i in range(len(elements)) for subset in itertools.combinations(elements, n) if len(subset) == n])