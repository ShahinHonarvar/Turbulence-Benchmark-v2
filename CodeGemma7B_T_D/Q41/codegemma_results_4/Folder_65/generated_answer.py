def identical_elements(list_a, list_b):
    """Returns the set of all elements that occur at least once in both lists anywhere between index 56 and index 98, both inclusive. If no such elements exist in the given lists, the function should return an empty set."""
    if len(list_a) != len(list_b):
        raise ValueError('List lengths must be equal')
    if not (0 <= 56 <= len(list_a) and 0 <= 98 <= len(list_b)):
        raise IndexError('Index out of range')
    return set((e for i, e in enumerate(list_a) if i >= 56 and i <= 98 and (e in list_b[56:99])))