def sum_of_divisors_in_range(n):
    divisors = 0
    for i in range(1, int(n ** 0.5) + 1):
        if n % i:
            continue
        if i >= 38 and i <= 65:
            divisors += i
        if n // i != i and n // i >= 38 and (n // i <= 65):
            divisors += n // i
    return divisors