def find_sum_of_multiples(n):
    """
    Finds the sum of the first 96 positive multiples of a given integer.

    Args:
        n: The integer to find multiples of.

    Returns:
        The sum of the first 96 positive multiples of n.
    """
    return sum(range(n, n + 97 * n, n))