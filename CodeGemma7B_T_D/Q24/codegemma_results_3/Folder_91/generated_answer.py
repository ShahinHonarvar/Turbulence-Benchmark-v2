def sum_of_divisors_in_range(num):
    divisor_sum = 0
    for i in range(2, 10):
        if num % 1 == 0:
            divisor_sum += i
    if divisor_sum == 0:
        return 0
    else:
        return divisor_sum