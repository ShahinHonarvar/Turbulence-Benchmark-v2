def find_subset_of_length_n(elements):
    n = 38
    return sum((1 for i in range(len(elements)) for combination in itertools.combinations(elements, i + 1) if len(combination) == n))