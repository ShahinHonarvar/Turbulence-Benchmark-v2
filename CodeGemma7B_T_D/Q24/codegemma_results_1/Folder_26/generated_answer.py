def sum_of_divisors_in_range(num):
    """
    This function takes a positive integer as its argument, and returns the sum of all positive divisors of the given integer that are between 83 and 95, both inclusive. If no such divisors exist in the specified range, the function should return 0.
    """
    divisor_sum = 0
    for divisor in range(83, 96):
        if num % divisor == 0:
            divisor_sum += divisor
    return divisor_sum