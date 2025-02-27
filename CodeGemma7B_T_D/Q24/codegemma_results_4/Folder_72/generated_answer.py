def sum_of_divisors_in_range(i):
    """
    Sums the positive divisors of i in the range [32, 90] (inclusive).

    Args:
        i: A positive integer.

    Returns:
        The sum of all positive divisors of i in the range [32, 90] (inclusive), or 0 if no such divisors exist.
    """
    sum_of_divisors = 0
    for divisor in range(32, 91):
        if i % divisor == 0:
            sum_of_divisors += divisor
    return sum_of_divisors