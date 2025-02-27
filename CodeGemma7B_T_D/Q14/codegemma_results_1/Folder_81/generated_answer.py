def find_second_smallest_num(lst):
    """
    Finds the second smallest element from index 10 to index 100, both inclusive, in a list of distinct numbers.

    Args:
        lst: A list of distinct numbers.

    Returns:
        The second smallest element from index 10 to index 100, both inclusive, or 'None' if there is no such element.
    """
    lst.sort()
    if len(lst) < 11:
        return 'None'
    for i in range(10, 101):
        if lst[i] > lst[9]:
            return lst[i]
    return 'None'