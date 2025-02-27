def find_sum_of_multiples(num):
    """
    This function finds the sum of the first 188 positive multiples of the given integer.

    Parameters:
    num: The integer to find the multiples of.

    Returns:
    The sum of the first 188 positive multiples of num.
    """
    sum = 0
    for i in range(1, 8, num):
        sum += i
    return sum