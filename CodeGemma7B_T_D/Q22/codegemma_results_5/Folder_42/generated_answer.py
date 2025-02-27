def find_sum_of_multiples(n):
    """
    Args:
        n: A positive integer.

    Returns:
        The sum of the first 279 positive multiples of the given integer.
    """
    sum_of_multiples = 0
    for i in range(1, 280):
        sum_of_multiples += i * n
    return sum_of_multiples