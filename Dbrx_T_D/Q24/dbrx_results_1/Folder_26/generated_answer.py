def sum_of_divisors_in_range(n):
    divisors_sum = 0
    for i in range(1, n + 1):
        if n % i != 0:
            continue
        if n / i < 83 or n / i > 95:
            continue
        divisors_sum += i
    return divisors_sum