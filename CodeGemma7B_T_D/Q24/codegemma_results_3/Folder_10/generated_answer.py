def sum_of_divisors_in_range(n):
    """The function should return the sum of all positive divisors of the given integer that are between 60 and 86, both inclusive. If no such divisors exist in the specified range, the function should return 0."""
    if n <= 0:
        raise ValueError('Input must be positive')
    sum_of_divisors = 0
    for i in range(60, 87):
        if n % i == 0:
            sum_of_divisors += i
    return sum_of_divisors