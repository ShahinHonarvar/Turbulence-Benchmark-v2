def find_sum_of_multiples(factor):
    """Finds the sum of the first 59 positive multiples of a given integer.

    Args:
        factor: The integer to find multiples of.

    Returns:
        The sum of the first 59 positive multiples of factor.
    """
    sum_of_multiples = 0
    for i in range(1, 60):
        sum_of_multiples += i * factor
    return sum_of_multiples