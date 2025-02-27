def find_second_largest_num(lst):
    """
    Finds the second largest element from index 59 to index 97, both inclusive.

    Args:
        lst: A list of distinct numbers.

    Returns:
        The second largest element from index 59 to index 97, both inclusive. If there is no such element, the function returns 'None'.
    """
    if not lst or len(lst) < 2:
        return None
    lst[59:98] = sorted(lst[59:98], reverse=True)
    if len(lst) < 99:
        return lst[98]
    for i in range(97, 58, -1):
        if lst[i] != lst[i - 1]:
            return lst[i - 1]
    return None