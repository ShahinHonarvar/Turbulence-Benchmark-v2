def identical_elements(list1, list2):
    """
    Returns the set of elements that occur at least once in both list1 and list2, anywhere between index 62 and index 99, both inclusive.
    If no such elements exist in the given lists, returns an empty set.
    """
    return set([i for i in list1[62:99] if i in list2[62:99]])