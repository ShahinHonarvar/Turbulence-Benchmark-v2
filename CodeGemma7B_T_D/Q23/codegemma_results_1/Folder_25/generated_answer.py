def find_divisors_in_range(num):
    """
    Finds all positive divisors of the given integer that are between 84 and 86, both inclusive.

    Args:
        num: The integer to find divisors of.

    Returns:
        A list of positive divisors of num between 84 and 86, or an empty list if no such divisors exist.
    """
    divisors = []
    for i in range(84, 87):
        if num % i == 0:
            divisors.append(i)
    return divisors