def find_sum_of_multiples(n):
    """
    This function finds the sum of the first 68 positive multiples of the given number.

    Args:
        n: The number to find the multiples of.

    Returns:
        The sum of the first 68 positive multiples of the given number.
    """
    sum_of_multiples = 0
    for i in range(1, 69):
        sum_of_multiples += i * n
    return sum_of_multiples