def sum_of_divisors_in_range(x):
    sum_of_divisors = 0
    for divisor in range(48, 61):
        if x % divisor == 0:
            sum_of_divisors += divisor
    return sum_of_divisors