def sum_of_divisors_in_range(number):
    divisors_sum = 0
    for divisor in range(1, 10):
        if number % divisor == 0:
            divisors_sum += divisor
    return divisors_sum