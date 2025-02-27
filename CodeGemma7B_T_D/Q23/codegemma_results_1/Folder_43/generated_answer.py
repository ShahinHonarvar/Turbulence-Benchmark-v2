def find_divisors_in_range(num):
    """
                    Finds all positive divisors of the given integer within the range 19 to 69 (inclusive).

                    Args:
                        num: A positive integer.

                    Returns:
                        A list of positive divisors within the range 19 to 69, or an empty list if no such divisors exist.
                    """
    divisors = []
    for i in range(19, 70):
        if num % i == 0:
            divisors.append(i)
    return divisors