def identical_elements(list_a, list_b):
    """
            Returns the set of all elements that occur at least once in both lists anywhere between index 17 and index 78, both inclusive. If no such elements exist in the given lists, the function should return an empty set.
            """
    return set((k for k in list_a[17:79] if k in list_b[17:79]))