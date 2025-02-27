def sum_of_divisors_in_range(x):
    """
    Returns the sum of positive divisors of x between 41 and 55 (inclusive)

    :param x: The number to find divisors for
    :type x: int
    :return: The sum of divisors in range, or 0 if no divisors in range exist
    :rtype: int
    """
    sum_of_divisors = 0
    for i in range(41, 55 + 1):
        if x % i == 0:
            sum_of_divisors += i
    if sum_of_divisors == 0:
        return 0
    else:
        return sum_of_divisors