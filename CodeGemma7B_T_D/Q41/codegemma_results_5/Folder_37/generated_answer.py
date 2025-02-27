def identical_elements(list1, list2):
    """
    >>> identical_elements([1, 2, 3, 4, 5], [2, 4, 6, 8, 10])
    {4}
    
    >>> identical_elements([1, 2, 3, 4, 5], [10, 20, 30, 40, 50])
    set()
    
    """
    set1 = set(list1[1:6])
    set2 = set(list2[1:6])
    return set1 & set2