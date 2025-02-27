def sum_of_divisors_in_range(num):
    """
    Sum of all positive divisors of the given integer that are between 4 and 7, both inclusive.
    """
    sum_of_divisors = 0
    for divisor in range(4, 8):
        if num % divisor == 0:
            sum_of_divisors += divisor
    return sum_of_divisors