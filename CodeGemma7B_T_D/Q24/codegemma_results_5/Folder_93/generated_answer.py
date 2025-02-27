def sum_of_divisors_in_range(num):
    """
    Returns the sum of all positive divisors of num between 48 and 92, inclusive.

    Args:
        num: A positive integer.

    Returns:
        The sum of all positive divisors of num between 48 and 92, inclusive, or 0 if no such divisors exist.
    """
    sum_of_divisors = 0
    for divisor in range(48, 93):
        if num % divisor == 0:
            sum_of_divisors += divisor
    return sum_of_divisors