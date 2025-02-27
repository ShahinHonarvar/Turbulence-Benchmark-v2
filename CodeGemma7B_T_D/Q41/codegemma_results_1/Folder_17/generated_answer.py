def identical_elements(list1, list2):
    """
            Finds the set of all elements that occur at least once in both lists anywhere between index 62 and index 78,
            inclusive. If no such elements exist in the given lists, returns an empty set.
            """
    elements = set(list1[62:79]) & set(list2[62:79])
    if not elements:
        elements = set()
    return elements