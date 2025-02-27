def sum_of_divisors_in_range(num):
    """
    This function takes a positive integer as its argument, and returns the sum of all positive divisors of the given integer that are between 32 and 35, both inclusive.

    If no such divisors exist in the specified range, the function should return 0.

    Args:
      num (int): The positive integer to find the divisors of.

    Returns:
      int: The sum of all positive divisors of the given integer that are between 32 and 35, both inclusive. If no such divisors exist in the specified range, the function should return 0.
    """
    divisors = []
    for i in range(32, 36):
        if num % i == 0:
            divisors.append(i)
    if len(divisors) == 0:
        return 0
    return sum(divisors)