def sum_of_divisors_in_range(num):
    total_sum = 0
    for divisor in range(472, 828):
        if num % divisor == 0:
            total_sum += divisor
    return total_sum