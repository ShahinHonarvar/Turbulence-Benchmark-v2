def sum_of_divisors_in_range(num):
    """
    Calculates the sum of all positive divisors of a number in a given range.

    Args:
        num: The positive integer to find divisors for.

    Returns:
        The sum of all positive divisors of the given integer in the range [35, 37], or 0 if no divisors are found.
    """
    divisors = []
    for i in range(35, 38):
        if num % i == 0:
            divisors.append(i)
    if not divisors:
        return 0
    return sum(divisors)