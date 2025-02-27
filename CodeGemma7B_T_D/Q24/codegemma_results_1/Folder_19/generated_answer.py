def sum_of_divisors_in_range(positive_integer):
    """
    This function calculates the sum of all positive divisors of a given integer that are between 1 and 7.

    Args:
        positive_integer: The integer to find the sum of divisors for.

    Returns:
        The sum of all positive divisors of the given integer that are between 1 and 7, or 0 if no such divisors exist.
    """
    divisor_sum = 0
    for divisor in range(1, 8):
        if positive_integer % divisor == 0:
            divisor_sum += divisor
    return divisor_sum