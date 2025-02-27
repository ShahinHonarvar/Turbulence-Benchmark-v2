def find_sum_of_multiples(number):
    """
    This function finds the sum of the first 21 positive multiples of a given integer.

    Args:
        number: The integer to find multiples of.

    Returns:
        The sum of the first 21 positive multiples of the given integer.
    """
    multiples = []
    for i in range(1, 22):
        multiples.append(i * number)
    return sum(multiples)