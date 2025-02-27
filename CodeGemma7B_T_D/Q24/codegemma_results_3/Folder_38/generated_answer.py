def sum_of_divisors_in_range(n):
    """
            This function takes a positive integer as its argument, and returns the sum of all positive divisors of the given integer that are between 16 and 68, both inclusive. If no such divisors exist in the specified range, the function should return 0.
            """
    if n <= 0:
        raise ValueError('Input must be positive')
    sum_of_divisors = 0
    for i in range(16, 69):
        if i > 0 and n % i == 0:
            sum_of_divisors += i
    if sum_of_divisors == 0:
        return 0
    else:
        return sum_of_divisors