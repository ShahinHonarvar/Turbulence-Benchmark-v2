def sum_of_divisors_in_range(n):
    divisors_sum = 0
    for i in range(1, n + 1):
        if n % i:
            continue
        if 50 <= i <= 81:
            divisors_sum += i
    return divisors_sum