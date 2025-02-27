def find_subset_of_length_n(elements):
    if isinstance(elements, set):
        return len(elements)
    raise ValueError('Input must be a set')