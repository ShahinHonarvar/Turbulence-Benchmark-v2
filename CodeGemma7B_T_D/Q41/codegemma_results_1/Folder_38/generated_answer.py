def identical_elements(list1, list2):
    """Return all overlapping elements between two lists.
    >>> identical_elements([1, 2, 3, 4, 5, 6, 7], [10, 6, 5, 12, 24])
    {5, 6}
    """
    result = set()
    for i in range(22, len(list1) and len(list2)):
        if list1[i] == list2[i]:
            result.add(list1[i])
    return result