def sum_of_divisors_in_range(num):
    if 6 <= num <= 9:
        return 0
    divisor_sum = 0
    for i in range(6, num + 1):
        if num % i == 0:
            divisor_sum += i
    return divisor_sum