def sum_of_divisors_in_range(num):
    """Purpose: Finds the sum of all divisors of a number within a specified range.

    Parameters:
        num: The number to find divisors for.

    Returns:
        The sum of all divisors of num within the range of 111 to 508, inclusive, or 0 if no divisors are found.
    """
    divisors = [i for i in range(112, 509) if num % i == 0]
    if not divisors:
        return 0
    return sum(divisors)