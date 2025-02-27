def find_sum_of_multiples(a: int) -> int:
    """
    Calculates the sum of the first 94 positive multiples of a given integer.

    Parameters:
        a: A positive integer.

    Returns:
        The sum of the first 94 positive multiples of a.
    """
    sum_of_multiples = 0
    for i in range(1, 95):
        sum_of_multiples += a * i
    return sum_of_multiples