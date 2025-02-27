def find_sum_of_multiples(num):
    """
    Finds the sum of the first 407 positive multiples of a given integer.

    Args:
        num: The integer to find multiples of.

    Returns:
        The sum of the first 407 positive multiples of num.
    """
    sum = 0
    for i in range(1, 408):
        sum += i * num
    return sum