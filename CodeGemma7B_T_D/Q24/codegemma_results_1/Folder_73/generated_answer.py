def sum_of_divisors_in_range(integer):
    divisor_sum = 0
    for divisor in range(46, 89 + 1):
        if integer % divisor == 0:
            divisor_sum += divisor
    if divisor_sum == 0:
        return 0
    else:
        return divisor_sum