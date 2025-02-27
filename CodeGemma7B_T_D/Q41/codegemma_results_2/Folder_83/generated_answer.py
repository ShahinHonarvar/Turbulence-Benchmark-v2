def identical_elements(list1, list2):
    """
    This function takes two arguments, two lists of the same size,
    and returns the set of all elements that occur at least once in both lists
    anywhere between index 90 and index 200, both inclusive.
    If no such elements exist in the given lists, the function should return an empty set.
    """
    set1 = set(list1[90:201])
    set2 = set(list2[90:201])
    return set1.intersection(set2)