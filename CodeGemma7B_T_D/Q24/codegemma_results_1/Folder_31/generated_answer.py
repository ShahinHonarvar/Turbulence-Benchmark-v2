def sum_of_divisors_in_range(number):
    divisor = 35
    if number <= 0:
        raise ValueError('Input must be positive integer')
    sum_of_divisors = 0
    while divisor <= 55:
        if number % divisor == 0:
            sum_of_divisors += divisor
        divisor += 1
    if sum_of_divisors == 0:
        return 0
    else:
        return sum_of_divisors