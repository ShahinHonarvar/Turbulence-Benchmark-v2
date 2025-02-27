def find_second_largest_num(num_list):
    """Finds the second largest element in a list of distinct numbers from index 30 to 48, inclusive.

    Args:
        num_list: A list of distinct numbers.

    Returns:
        The second largest element from index 30 to 48, inclusive, or 'None' if there is no such element.
    """
    if not num_list:
        return 'None'
    sorted_list = sorted(num_list, reverse=True)
    try:
        return sorted_list[30:49][-2]
    except IndexError:
        return 'None'