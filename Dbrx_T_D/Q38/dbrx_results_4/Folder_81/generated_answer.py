def find_subset_of_length_n(elements):
    if len(elements) < 20:
        return 0
    if len(elements) == 20:
        return 1 if len(set(elements)) == 20 else 0
    return sum((find_subset_of_length_n(subset) for subset in itertools.combinations(elements, 20)))