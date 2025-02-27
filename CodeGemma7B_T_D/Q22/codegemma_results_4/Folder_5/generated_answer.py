def find_sum_of_multiples(num):
    """Finds the sum of the first 13 multiples of a number.

    Args:
        num: A positive integer.

    Returns:
        The sum of the first 13 multiples of num.
    """
    sum = 0
    for i in range(1, 14):
        sum += i * num
    return sum