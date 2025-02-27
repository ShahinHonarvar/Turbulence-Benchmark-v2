def sum_of_divisors_in_range(num):
    divisors_sum = 0
    for divisor in range(1, num + 1):
        if num % divisor == 0 and 84 <= divisor <= 86:
            divisors_sum += divisor
    return divisors_sum