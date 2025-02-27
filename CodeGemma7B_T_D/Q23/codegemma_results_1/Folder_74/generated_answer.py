def find_divisors_in_range(num):
    """
    Finds the divisors of a number in a given range.

    Args:
        num: The number to find the divisors of.

    Returns:
        A list of positive divisors of the given number that are between 40 and 74, both inclusive. If no such divisors exist, the function returns an empty list.
    """
    divisors = []
    for divisor in range(40, 75):
        if num % divisor == 0:
            divisors.append(divisor)
    return divisors