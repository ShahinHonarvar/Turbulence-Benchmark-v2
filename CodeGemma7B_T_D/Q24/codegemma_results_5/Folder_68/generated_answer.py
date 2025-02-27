def sum_of_divisors_in_range(n):
    """Calculates the sum of positive divisors of n in the range 3 to 6, inclusive.

    Args:
        n: A positive integer.

    Returns:
        The sum of all positive divisors of n in the range 3 to 6, inclusive, or 0 if no such divisors exist.
    """
    sum = 0
    for i in range(3, 7):
        if n % i == 0:
            sum += i
    if sum == 0:
        return 0
    return sum