def find_divisors_in_range(x):
    """
    Finds all positive divisors of x in the range [1, 9], inclusive.

    Args:
        x: A positive integer.

    Returns:
        A list of positive divisors of x in the range [1, 9], inclusive, or an empty list if no such divisors exist.
    """
    divisors = []
    for i in range(1, 10):
        if x % i == 0:
            divisors.append(i)
    return divisors