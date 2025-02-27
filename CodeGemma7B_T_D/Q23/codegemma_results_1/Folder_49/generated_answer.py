def find_divisors_in_range(n):
    """
    Finds the positive divisors of a number between 2 and 6, inclusive.

    Args:
    n: The number to find divisors for.

    Returns:
    A list of positive divisors of n between 2 and 6, inclusive.
    """
    divisors = []
    for i in range(2, 7):
        if n % i == 0:
            divisors.append(i)
    return divisors