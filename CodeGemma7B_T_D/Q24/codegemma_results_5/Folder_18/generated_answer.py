def sum_of_divisors_in_range(n):
    """
    This function takes a positive integer as its argument, and returns the sum of all positive divisors of the given integer that are between 387 and 516, both inclusive. If no such divisors exist in the specified range, the function should return 0.
    """
    return sum([i for i in range(387, 517) if n % i == 0])