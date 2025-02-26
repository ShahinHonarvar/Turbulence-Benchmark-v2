def sum_of_divisors_in_range(n):
    total = 0
    for divisor in range(461, 828):
        if n % divisor == 0:
            total += divisor
    return total