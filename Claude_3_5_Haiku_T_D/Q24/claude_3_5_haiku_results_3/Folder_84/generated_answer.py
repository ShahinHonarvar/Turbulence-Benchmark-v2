def sum_of_divisors_in_range(number):
    divisor_sum = 0
    for divisor in range(224, 585):
        if number % divisor == 0:
            divisor_sum += divisor
    return divisor_sum