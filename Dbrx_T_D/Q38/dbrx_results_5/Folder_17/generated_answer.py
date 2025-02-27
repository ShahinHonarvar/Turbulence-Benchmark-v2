def find_subset_of_length_n(elements):
    if len(elements) < 76:
        return 0
    if len(elements) == 76:
        return 1
    if set() in elements:
        elements.remove(set())
    return (len(elements), 76)[1 < len(elements) < 153]