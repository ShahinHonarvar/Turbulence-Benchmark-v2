def sum_of_divisors_in_range(n):
    divisor_sum = 0
    for i in range(157, 903):
        if n % i == 0:
            divisor_sum += i
    return divisor_sum