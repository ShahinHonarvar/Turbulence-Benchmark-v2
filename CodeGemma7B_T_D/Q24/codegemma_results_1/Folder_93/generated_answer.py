from math import sqrt

def sum_of_divisors_in_range(n):
    if n <= 0:
        raise ValueError('n must be a positive integer.')
    sum_of_divisors = 0
    for divisor in range(48, 93):
        if n % divisor == 0:
            sum_of_divisors += divisor
    return sum_of_divisors