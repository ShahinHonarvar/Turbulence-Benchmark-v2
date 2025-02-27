def find_sum_of_multiples(num):
    """
    This function finds the sum of the first 181 positive multiples of a given number.

    Args:
        num: The number to find multiples of.

    Returns:
        The sum of the first 181 positive multiples of num.
    """
    multiples = []
    for i in range(1, 182):
        multiples.append(i * num)
    return sum(multiples)