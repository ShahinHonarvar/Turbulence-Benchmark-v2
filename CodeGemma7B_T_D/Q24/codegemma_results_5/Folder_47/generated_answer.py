def sum_of_divisors_in_range(num):
    sum_of_div = 0
    for divisor in range(27, 45):
        if num % divisor == 0:
            sum_of_div += divisor
    if sum_of_div == 0:
        return 0
    else:
        return sum_of_div