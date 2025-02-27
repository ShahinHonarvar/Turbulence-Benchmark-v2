def sum_of_divisors_in_range(num):
    """
    Calculates the sum of all positive divisors of a number in a specified range.

    Args:
        num: The integer to find divisors for.

    Returns:
        The sum of all divisors in the specified range, or 0 if no divisors are found.
    """
    divisors = []
    for i in range(83, 96):
        if num % i == 0:
            divisors.append(i)
    if not divisors:
        return 0
    return sum(divisors)