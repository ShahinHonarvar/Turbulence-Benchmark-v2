def find_subset_of_length_n(elements):
    if len(elements) < 54:
        return 0
    if len(elements) == 54:
        return 1
    return sum((find_subset_of_length_n(subset) for subset in combinations(elements, 54)))