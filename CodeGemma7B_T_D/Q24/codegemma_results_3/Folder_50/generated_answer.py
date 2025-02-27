def sum_of_divisors_in_range(n):
    """ 
        Given a positive integer, return the sum of all positive divisors of the given integer
        that are between 57 and 86, both inclusive. If no such divisors exist in the specified range, the function should return 0. 
    """
    limit_min = 57
    limit_max = 86
    sum_of_divisors = 0
    for divisor in range(limit_min, limit_max + 1):
        if n % divisor == 0:
            sum_of_divisors += divisor
    return sum_of_divisors if sum_of_divisors else 0