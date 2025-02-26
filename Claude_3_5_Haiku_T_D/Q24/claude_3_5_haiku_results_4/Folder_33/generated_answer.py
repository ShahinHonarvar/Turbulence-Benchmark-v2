def sum_of_divisors_in_range(n):
    divisor_sum = 0
    for div in range(157, 903):
        if n % div == 0:
            divisor_sum += div
    return divisor_sum