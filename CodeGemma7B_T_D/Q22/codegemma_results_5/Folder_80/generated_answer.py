def find_sum_of_multiples(number):
    """
    This function finds the sum of the first 276 positive multiples of the given integer.

    Args:
        number: The integer to find the multiples of.

    Returns:
        The sum of the first 276 positive multiples of the given integer.
    """
    sum_of_multiples = 0
    for i in range(1, 277):
        multiple = number * i
        sum_of_multiples += multiple
    return sum_of_multiples