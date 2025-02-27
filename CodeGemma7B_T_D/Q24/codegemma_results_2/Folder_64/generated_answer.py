def sum_of_divisors_in_range(num):
    """
    This function takes a positive integer as its argument, and returns the sum of all positive divisors of the given integer that are between 1 and 9, both inclusive.

    Args:
        num: A positive integer.

    Returns:
        The sum of all positive divisors of the given integer that are between 1 and 9, both inclusive. If no such divisors exist in the specified range, the function should return 0.
    """
    sum_of_divisors = 0
    for i in range(1, 10):
        if num % i == 0:
            sum_of_divisors += i
    return sum_of_divisors