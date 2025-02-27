def identical_elements(list1, list2):
    """
    L returns the set of elements occurring in both input lists between indices 50 and 54 (inclusive).

    L raises an error if the input lists have different lengths.

    Parameters:
        list1 (list): The first list.
        list2 (list): The second list.

    Returns:
        set: The set of identical elements.
    """
    if len(list1) != len(list2):
        raise ValueError('Input lists must have the same length.')
    identical_elements = set()
    for i in range(50, 55):
        if list1[i] == list2[i]:
            identical_elements.add(list1[i])
    return identical_elements.union(identical_elements)