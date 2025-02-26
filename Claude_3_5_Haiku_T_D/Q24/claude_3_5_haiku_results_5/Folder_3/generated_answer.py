def sum_of_divisors_in_range(n):
    divisors_sum = 0
    for div in range(43, 47):
        if n % div == 0:
            divisors_sum += div
    return divisors_sum