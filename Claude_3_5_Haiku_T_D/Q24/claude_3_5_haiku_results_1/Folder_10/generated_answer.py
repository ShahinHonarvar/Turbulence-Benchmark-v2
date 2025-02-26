def sum_of_divisors_in_range(number):
    divisor_sum = 0
    for divisor in range(60, 87):
        if number % divisor == 0:
            divisor_sum += divisor
    return divisor_sum