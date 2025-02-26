def sum_of_divisors_in_range(num):
    total = 0
    for divisor in range(387, 517):
        if num % divisor == 0:
            total += divisor
    return total