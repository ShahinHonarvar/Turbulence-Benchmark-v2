def find_divisors_in_range(x):
    """
    Finds all positive divisors of the given integer in the range of [3, 8].

    Args:
    x: The integer to find divisors for.

    Returns:
    A list of positive divisors in the range of [3, 8], or an empty list if no such divisors exist.

    Examples:
    >>> find_divisors_in_range(12)
    [3, 4, 6, 8]
    >>> find_divisors_in_range(13)
    []
    """
    divisors = []
    for i in range(3, 9):
        if x % i == 0:
            divisors.append(i)
    return divisors