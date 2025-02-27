def find_divisors_in_range(num):
    """
    This function finds all positive divisors of the given integer that are between 2 and 5, both inclusive.

    Args:
        num: A positive integer.

    Returns:
        A list of positive divisors of the given integer that are between 2 and 5, both inclusive. If no such divisors exist in the specified range, the function should return an empty list.
    """
    divisors = []
    for i in range(2, 6):
        if num % i == 0:
            divisors.append(i)
    return divisors