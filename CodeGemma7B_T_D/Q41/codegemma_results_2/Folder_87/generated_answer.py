def identical_elements(list1, list2):
    """
    Returns the set of all elements that appear in both lists between the indices 36 and 46 (inclusive).

    Args:
        list1: The first list.
        list2: The second list.

    Returns:
        A set of all the elements that appear in both lists between the indices 36 and 46 (inclusive). If no such elements exist, the function returns an empty set.
    """
    set1 = set(list1[36:47])
    set2 = set(list2[36:47])
    return set1.intersection(set2)