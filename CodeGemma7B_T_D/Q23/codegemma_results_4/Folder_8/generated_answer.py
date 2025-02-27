def find_divisors_in_range(num):
    """
    Finds all positive divisors of a given integer in the range [48, 62].

    Args:
        num: The integer to find divisors for.

    Returns:
        A list of positive divisors of num in the range [48, 62], or an empty list if no such divisors exist.
    """
    divisors = []
    for i in range(48, 63):
        if num % i == 0:
            divisors.append(i)
    return divisors