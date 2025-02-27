def sum_of_divisors_in_range(num):
    divisor_sum = 0
    for divisor in range(3, 10):
        if num % divisor == 0:
            divisor_sum += divisor
    return divisor_sum if divisor_sum != 0 else 0