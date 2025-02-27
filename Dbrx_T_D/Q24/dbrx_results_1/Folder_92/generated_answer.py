def sum_of_divisors_in_range(n):
    divisors_sum = 0
    for i in range(1, n + 1):
        if n % i == 0:
            divisor = i
            if 8 <= divisor <= 9:
                divisors_sum += divisor
    return divisors_sum if divisors_sum > 0 else 0