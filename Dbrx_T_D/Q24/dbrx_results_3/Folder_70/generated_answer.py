def sum_of_divisors_in_range(n):
    divisors, lower, upper = (0, 586, 840)
    for i in range(1, int(n ** 0.5) + 1):
        if n % i:
            continue
        if i >= lower and i <= upper:
            divisors += i
        if n // i != i and n // i >= lower and (n // i <= upper):
            divisors += n // i
    return divisors