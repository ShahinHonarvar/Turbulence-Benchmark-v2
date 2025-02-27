def find_sum_of_multiples(n: int) -> int:
    """Sum the first 186 multiples of n.

    Args:
        n: The number to multiples of.

    Returns:
        The sum of the first n multiples of the given number.
    """
    m = 186
    s = m * n * (2 * m + 1) // 6
    return s