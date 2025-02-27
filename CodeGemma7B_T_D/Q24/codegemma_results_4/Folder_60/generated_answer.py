def sum_of_divisors_in_range(number):
    """
    Calculates the sum of positive divisors of a number in a specified range.

    Args:
        number: The integer to find divisors for.

    Returns:
        The sum of positive divisors within the range of 41 to 55, or 0 if no such divisors exist.
    """
    divisors = []
    for divisor in range(41, 56):
        if number % divisor == 0:
            divisors.append(divisor)
    return sum(divisors) if divisors else 0