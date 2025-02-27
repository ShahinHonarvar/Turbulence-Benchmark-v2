def find_divisors_in_range(number):
    """
    Finds all positive divisors of the given number that are between 39 and 57, both inclusive.

    Args:
        number: The number to find divisors for.

    Returns:
        A list of positive divisors between 39 and 57 inclusive, or an empty list if no such divisors exist.
    """
    divisors = []
    for i in range(39, 58):
        if number % i == 0:
            divisors.append(i)
    return divisors