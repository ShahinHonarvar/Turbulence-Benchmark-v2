def sum_of_divisors_in_range(num):
    sum_of_divisors = 0
    for divisor in range(16, 69):
        if num % divisor == 0:
            sum_of_divisors += divisor
    return sum_of_divisors