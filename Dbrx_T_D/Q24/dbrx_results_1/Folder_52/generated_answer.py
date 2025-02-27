def sum_of_divisors_in_range(n):
    divisors_sum = 0
    for divisor in range(1, int(n ** 0.5) + 1):
        if n % divisor != 0:
            continue
        other_divisor = n // divisor
        if 70 <= divisor <= 72:
            divisors_sum += divisor
        elif 70 <= other_divisor <= 72:
            divisors_sum += other_divisor
    return divisors_sum