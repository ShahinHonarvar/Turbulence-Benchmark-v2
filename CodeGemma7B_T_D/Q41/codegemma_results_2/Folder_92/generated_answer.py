def identical_elements(list1, list2):
    """
    This function takes two lists of the same size as input and returns the set of elements that are present in both lists.

    Args:
        list1 (list): The first list.
        list2 (list): The second list.

    Returns:
        set: The set of elements that are present in both lists.
    """
    index = 0
    set_of_elements = set()
    for element1, element2 in zip(list1, list2):
        if element1 == element2:
            set_of_elements.add(element1)
            index += 1
    return set_of_elements