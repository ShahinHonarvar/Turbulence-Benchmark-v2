def sum_of_divisors_in_range(n):
    divisor_sum = 0
    for i in range(461, 828):
        if i % n == 0:
            divisor_sum += i
    if divisor_sum == 0:
        return 0
    return divisor_sum