def sum_of_divisors_in_range(n):
    """
    Returns the sum of all positive divisors of the given integer
    that are between 120 and 349, both inclusive. If no such divisors exist
    in the specified range, the function should return 0.
    """
    divisor_sum = 0
    for i in range(1, n + 1):
        if n % i == 0 and i in range(120, 350):
            divisor_sum += i
    return divisor_sum