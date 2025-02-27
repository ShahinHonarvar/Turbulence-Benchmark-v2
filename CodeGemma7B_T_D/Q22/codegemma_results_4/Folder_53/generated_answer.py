def find_sum_of_multiples(n):
    """
    This function finds the sum of the first 60 positive multiples of the given integer.

    Args:
        n: The integer to find multiples of.

    Returns:
        The sum of the first 60 positive multiples of the given integer.
    """
    sum = 0
    for i in range(1, 61):
        sum += n * i
    return sum