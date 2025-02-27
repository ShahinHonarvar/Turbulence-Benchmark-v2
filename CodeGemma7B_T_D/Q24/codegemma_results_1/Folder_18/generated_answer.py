def sum_of_divisors_in_range(num):
    result = 0
    for divisor in range(387, 517):
        if num % divisor == 0:
            result += divisor
    return result