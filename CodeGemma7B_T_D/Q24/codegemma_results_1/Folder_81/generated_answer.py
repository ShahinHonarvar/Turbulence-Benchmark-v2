def sum_of_divisors_in_range(n):
    """
            Takes a positive integer as its argument and returns the sum of all
            positive divisors of the given integer that are between 3 and 4, both inclusive.
            If no such divisors exist in the specified range, the function should return 0.
            """
    sum_of_divisors = 0
    for divisor in range(3, 5):
        if n % divisor == 0:
            sum_of_divisors += divisor
    return sum_of_divisors if sum_of_divisors else 0