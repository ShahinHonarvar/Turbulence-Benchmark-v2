def sum_of_divisors_in_range(num):
    """Given a positive integer, return sum of all positive divisors of the number within range of 33 to 57.

    Args:
      num: The number for which we find the sum of divisors.

    Returns:
      Return sum of all factors of num between 33 and 57, otherwise 0
    """
    sum_div = 0
    for factor in range(33, 58):
        if num % factor == 0:
            sum_div += factor
    return sum_div if sum_div > 0 else 0