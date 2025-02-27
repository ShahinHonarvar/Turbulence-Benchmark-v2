def identical_elements(list1, list2):
    """
    This function takes two lists of the same size, finds all elements that occur at least once in both lists anywhere between index 75 and index 94, and returns their set.
    """
    return set([x for x in list1[75:95] if x in list2[75:95]])