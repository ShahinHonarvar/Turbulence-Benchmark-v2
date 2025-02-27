def sum_of_divisors_in_range(n):
    divisors = 0
    for i in range(1, n + 1):
        if n % i != 0:
            continue
        if i >= 111 and i <= 508:
            divisors += i
    return divisors if divisors != 0 else 0