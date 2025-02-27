from math import sqrt

def sum_of_divisors_in_range(n):
    """
    Calculates the sum of divisors within a specific range for a given integer.
    """
    sum_divisors = 0
    for divisor in range(127, int(sqrt(n)) + 1):
        if n % divisor == 0:
            if divisor in range(113, 992):
                sum_divisors += divisor
                if n // divisor not in range(113, 992):
                    sum_divisors += n // divisor
    return sum_divisors