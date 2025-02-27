def identical_elements(list1: list, list2: list) -> set:
    """
    Returns the set of all elements that occur at least once in both lists anywhere between index 23 and index 23, both inclusive. If no such elements exist in the given lists, the function should return an empty set.
    """
    if len(list1) != len(list2) or len(list1) < 47 or len(list2) < 47:
        raise ValueError('The lists should have the same size and be larger than 46 elements.')
    set1 = set(list1[23:47])
    set2 = set(list2[23:47])
    return set1.intersection(set2)