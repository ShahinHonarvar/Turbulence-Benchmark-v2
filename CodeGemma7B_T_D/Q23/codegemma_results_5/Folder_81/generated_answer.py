def find_divisors_in_range(a):
    """
    Finds all positive divisors of a given integer in the specified range.

    Args:
    a: The integer to find divisors of.

    Returns:
    A list of positive divisors of a in the range [3, 4], or an empty list if no such divisors exist.
    """
    divisors = []
    for i in range(3, 5):
        if a % i == 0:
            divisors.append(i)
    return divisors