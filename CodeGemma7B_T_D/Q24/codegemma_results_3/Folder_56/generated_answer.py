from math import sqrt

def sum_of_divisors_in_range(num):
    divisor_sum = 0
    limit = sqrt(num) + 1
    for divisor in range(6, limit):
        if num % divisor == 0:
            divisor_sum += divisor
            if divisor != num // divisor:
                divisor_sum += num // divisor
    return divisor_sum