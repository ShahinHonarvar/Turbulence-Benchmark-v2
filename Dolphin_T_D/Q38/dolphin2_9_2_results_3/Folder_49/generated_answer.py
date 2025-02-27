def find_subset_of_length_n(n, elements):
    if len(elements) < n:
        return 0
    return elements.count(n)