def sum_of_divisors_in_range(num):
    divisor = 43
    divisor_sum = 0
    while divisor <= 46:
        if num % divisor == 0:
            divisor_sum += divisor
        divisor += 1
    return divisor_sum