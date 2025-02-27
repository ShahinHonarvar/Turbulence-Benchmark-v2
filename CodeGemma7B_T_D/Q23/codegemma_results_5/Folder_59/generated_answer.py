def find_divisors_in_range(number):
    """
    Finds all positive divisors of a number between 3 and 5, inclusive.

    Args:
      number: A positive integer.

    Returns:
      A list of positive divisors of the given number between 3 and 5, inclusive. If no such divisors exist, an empty list is returned.
    """
    divisors = []
    for i in range(3, 6):
        if number % i == 0:
            divisors.append(i)
    return divisors