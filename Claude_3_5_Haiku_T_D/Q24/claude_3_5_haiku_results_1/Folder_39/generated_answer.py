def sum_of_divisors_in_range(n):
    total_sum = 0
    for divisor in range(11, 57):
        if n % divisor == 0:
            total_sum += divisor
    return total_sum