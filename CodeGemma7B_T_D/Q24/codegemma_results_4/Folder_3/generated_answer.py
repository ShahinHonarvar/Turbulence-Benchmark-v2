def sum_of_divisors_in_range(num):
    """
    This function takes a positive integer as its argument, and returns the sum of all positive divisors of the given integer that are between 43 and 46, both inclusive. If no such divisors exist in the specified range, the function should return 0.

    Args:
        num: The positive integer to find the sum of divisors for.

    Returns:
        The sum of all positive divisors of the given integer that are between 43 and 46, both inclusive. If no such divisors exist in the specified range, the function should return 0.
    """
    if num <= 0:
        raise ValueError('Input number must be positive.')
    sum_divisors = 0
    for i in range(43, 47):
        if num % i == 0:
            sum_divisors += i
    return sum_divisors