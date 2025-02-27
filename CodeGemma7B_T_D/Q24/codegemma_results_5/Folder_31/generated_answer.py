def sum_of_divisors_in_range(num):
    if not isinstance(num, int) or num <= 0:
        raise ValueError('Invalid input: argument must be a positive integer')
    sum_of_divisors = 0
    for divisor in range(35, 56):
        if num % divisor == 0:
            sum_of_divisors += divisor
    return sum_of_divisors