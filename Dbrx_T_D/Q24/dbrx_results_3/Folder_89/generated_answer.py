def sum_of_divisors_in_range(n):
    divisors_sum = 0
    for i in range(1, n + 1):
        if n % i:
            continue
        if 14 <= i <= 48:
            divisors_sum += i
    return divisors_sum if divisors_sum > 0 else 0