def identical_elements(list1, list2):
    """
    This function takes two lists of the same size as arguments and returns the set of all
    elements that occur at least once in both lists anywhere between index 9 and index 9, both
    inclusive. If no such elements exist in the given lists, the function returns an empty set.
    """
    set1 = set(list1[9:10])
    set2 = set(list2[9:10])
    intersection = set1 & set2
    return intersection if intersection else set()