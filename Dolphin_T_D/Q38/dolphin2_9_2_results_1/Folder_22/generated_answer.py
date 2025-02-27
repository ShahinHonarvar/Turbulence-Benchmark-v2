def find_subset_of_length_n(elements):
    if len(elements) < 72:
        return 0
    n = len(elements)
    return elements.combination(72)