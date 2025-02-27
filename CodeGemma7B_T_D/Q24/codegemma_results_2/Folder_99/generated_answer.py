def sum_of_divisors_in_range(num):
    divisor_sum = 0
    for divisor in range(378, 783):
        if num % divisor == 0:
            divisor_sum += divisor
    if divisor_sum == 0:
        return 0
    return divisor_sum