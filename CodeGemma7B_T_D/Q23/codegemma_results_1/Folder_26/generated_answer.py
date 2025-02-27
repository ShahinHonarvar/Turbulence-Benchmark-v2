def find_divisors_in_range(x):
    """
    Finds all positive divisors of the given integer that are between 83 and 95, both inclusive.

    Args:
        x: The integer to find divisors of.

    Returns:
        A list of positive divisors of x that are between 83 and 95, both inclusive. If no such divisors exist, the function returns an empty list.
    """
    divisors = []
    for i in range(83, 96):
        if x % i == 0:
            divisors.append(i)
    return divisors