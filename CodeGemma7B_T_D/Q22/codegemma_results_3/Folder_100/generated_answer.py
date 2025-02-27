def find_sum_of_multiples(num):
    """
    Finds the sum of the first 91 positive multiples of a given integer.

    Args:
        num: The integer to find multiples of.

    Returns:
        The sum of the first 91 positive multiples of the given integer.
    """
    sum_multiples = 0
    for i in range(1, 92):
        multiples = num * i
        sum_multiples += multiples
    return sum_multiples