def find_divisors_in_range(n):
    """
    Finds all positive divisors of a number that are between 469 and 682, inclusive.

    Args:
    n: The number to find divisors for.

    Returns:
    A list of positive divisors of n that are between 469 and 682, inclusive, or
    an empty list if no such divisors exist in the specified range.
    """
    divisors = []
    for i in range(469, 683):
        if n % i == 0:
            divisors.append(i)
    return divisors