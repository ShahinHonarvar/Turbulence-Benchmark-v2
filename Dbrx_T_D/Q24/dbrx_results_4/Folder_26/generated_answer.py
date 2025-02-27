def sum_of_divisors_in_range(n):
    divisors_sum = 0
    for i in range(1, n + 1):
        if n % i != 0:
            continue
        if 83 <= i <= 95:
            divisors_sum += i
    return divisors_sum