def sum_of_divisors_in_range(num):
    if num <= 0:
        raise ValueError('Input number must be positive.')
    sum_of_divisors = 0
    for divisor in range(461, 828):
        if num % divisor == 0:
            sum_of_divisors += divisor
    return sum_of_divisors or 0