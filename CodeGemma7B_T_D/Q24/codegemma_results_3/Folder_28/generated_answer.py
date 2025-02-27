def sum_of_divisors_in_range(num):
    divisor_sum = 0
    for i in range(16, 54):
        if num % i == 0:
            divisor_sum += i
    if divisor_sum == 0:
        return 0
    return divisor_sum