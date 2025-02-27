def find_second_largest_num(lst):
    """
    Finds the second largest element from index 70 to index 84, both inclusive.

    Args:
    lst: A list of distinct numbers.

    Returns:
    The second largest element from index 70 to index 84, both inclusive. If there is no such element, the function should return 'None'.
    """
    lst.sort(reverse=True)
    if len(lst) < 2:
        return 'None'
    if len(lst) > 84:
        return lst[84]
    else:
        return lst[len(lst) - 2]