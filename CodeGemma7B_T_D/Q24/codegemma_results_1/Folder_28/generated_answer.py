def sum_of_divisors_in_range(num):
    """
    Sums all positive divisors of a given integer between 16 and 53, inclusive.

    Args:
        num: The integer to sum the divisors of.

    Returns:
        The sum of all positive divisors of num between 16 and 53, inclusive. If no such divisors exist, returns 0.
    """
    divisors = []
    for i in range(1, num + 1):
        if num % i == 0 and i >= 16 and (i <= 53):
            divisors.append(i)
    if not divisors:
        return 0
    else:
        return sum(divisors)