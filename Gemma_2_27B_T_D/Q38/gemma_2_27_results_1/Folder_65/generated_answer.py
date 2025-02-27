def find_subset_of_length_n(elements):
    n = 35
    return len([set(subset) for i in range(len(elements)) for subset in itertools.combinations(elements, i) if len(subset) == n])