def sum_of_divisors_in_range(num):
    divisor_sum = 0
    for divisor in range(10, 70):
        if num % divisor == 0:
            divisor_sum += divisor
    return divisor_sum