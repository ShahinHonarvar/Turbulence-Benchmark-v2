def sum_of_divisors_in_range(num):
    total = 0
    for divisor in range(472, 828):
        if num % divisor == 0:
            total += divisor
    return total or 0