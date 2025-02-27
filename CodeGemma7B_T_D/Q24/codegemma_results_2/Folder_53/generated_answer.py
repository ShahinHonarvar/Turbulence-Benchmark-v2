def sum_of_divisors_in_range(num):
    sum_divisors = 0
    for divisor in range(4, 10):
        if num % divisor == 0:
            sum_divisors += divisor
    return sum_divisors