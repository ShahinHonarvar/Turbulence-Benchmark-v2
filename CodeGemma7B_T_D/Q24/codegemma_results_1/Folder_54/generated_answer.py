def sum_of_divisors_in_range(n):
    """Return the sum of all positive divisors of a given integer between 36 and 93, inclusive."""
    sum_div = 0
    for divisor in range(36, 94):
        if n % divisor == 0:
            sum_div += divisor
    if sum_div == 0:
        return 0
    else:
        return sum_div