def sum_in_range(lst):
    """
    Calculates the sum of all integers in a list that are between 273 and 451, inclusive.

    Parameters:
    lst (list): A list of integers.

    Returns:
    int: The sum of all integers from the given list that are between 273 and 451, inclusive. If the given list does not contain such integers, the function should return 0.
    """
    total = 0
    for i in lst:
        if i >= 273 and i <= 451:
            total += i
    return total