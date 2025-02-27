def find_divisors_in_range(number: int) -> list[int]:
    """
    Finds all positive divisors of a given integer in the range 1 to 7, inclusive.

    Args:
        number: The integer to search for divisors.

    Returns:
        A list of all positive divisors of the given integer in the range 1 to 7, inclusive. If no such divisors exist, an empty list is returned.
    """
    divisors = []
    for i in range(1, 8):
        if number % i == 0:
            divisors.append(i)
    return divisors