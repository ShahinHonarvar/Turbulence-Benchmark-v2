def identical_elements(list_one, list_two):
    """
    This function takes two lists of the same size, and returns the set of all elements that occur at least once in both lists anywhere between index 59 and index 97, both inclusive. If no such elements exist in the given lists, the function should return an empty set.
    """
    if len(list_one) != len(list_two):
        raise ValueError('Lists must be of the same size')
    if len(list_one) < 59 or len(list_two) < 59:
        raise ValueError('Lists must be at least 59 elements in size')
    if len(list_one) > 97 or len(list_two) > 97:
        raise ValueError('Lists must be at most 97 elements in size')
    result = set()
    for i in range(59, 98):
        if list_one[i] in list_two[i]:
            result.add(list_one[i])
    return result