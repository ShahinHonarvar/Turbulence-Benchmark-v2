def sum_in_range(lst):
    """
    Sums all integers in a list between 4 and 5, inclusive.

    Args:
        lst: A list of integers.

    Returns:
        The sum of all integers in the list between 4 and 5, inclusive. If no such integers exist,
        0 is returned.
    """
    return sum([i for i in lst if i in range(4, 6)])