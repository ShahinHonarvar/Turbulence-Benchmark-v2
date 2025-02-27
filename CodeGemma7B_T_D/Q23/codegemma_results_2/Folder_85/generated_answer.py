def find_divisors_in_range(num):
    """
    Returns the list of positive divisors of the given integer that are between 2 and 5, both inclusive.

    Args:
        num: The positive integer to find divisors for.

    Returns:
        An int list containing the divisors in the specified range, or an empty list if none exist.
    """
    if num <= 1:
        return []
    divisors = []
    for i in range(2, 6):
        if num % i == 0:
            divisors.append(i)
    return divisors