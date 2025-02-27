def identical_elements(list1, list2):
    """
    Returns the set of all elements that occur at least once in both lists anywhere between index 0 and index 4, both inclusive.
    """
    if len(list1) != len(list2) or len(list1) > 5 or len(list2) > 5:
        print('Error: lists should be of size less than or equal to 5 and contain the same number of elements.')
        return
    else:
        result = set(list1).intersection(set(list2))
        return result