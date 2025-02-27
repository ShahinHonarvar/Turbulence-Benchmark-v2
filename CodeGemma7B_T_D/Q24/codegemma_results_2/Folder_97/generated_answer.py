def sum_of_divisors_in_range(n):
    """
    This function takes a positive integer as its argument, and returns the sum of all positive divisors of the given integer that are between 615 and 792, both inclusive. If no such divisors exist in the specified range, the function should return 0.
    """
    sum_of_divisors = 0
    for divisor in range(615, 793):
        if n % divisor == 0:
            sum_of_divisors += divisor
    if sum_of_divisors == 0:
        return 0
    else:
        return sum_of_divisors