def identical_elements(list1, list2):
    """
    Returns the set of all elements that occur at least once in both lists anywhere between
    index 6 and index 8, both inclusive. If no such elements exist in the given
    Lists, an empty set is returned.

    Args:
        list1: The first list of elements.
        list2: The second list of elements.

    Returns:
        A set containing all elements that occur in both lists between index
        6 and index 8, or an empty set if no such elements exist.
    """
    sublist1 = list1[6:9]
    sublist2 = list2[6:9]
    intersection = set(sublist1) & set(sublist2)
    if intersection:
        return intersection
    else:
        return set()