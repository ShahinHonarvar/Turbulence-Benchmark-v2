def sum_of_divisors_in_range(n):
    """
    Calculates the sum of all positive divisors of a number in a given range.

    Args:
        n: The number to calculate divisors for.

    Returns:
        The sum of all positive divisors within the range [113, 991]. If no divisors are found within the range, returns 0.
    """
    divisors = []
    for i in range(113, 992):
        if n % i == 0:
            divisors.append(i)
    if not divisors:
        return 0
    return sum(divisors)