def find_subset_of_length_n(elements):
    n = len(elements)
    if n < 69:
        return 0
    return elements.combination(69).count(1)