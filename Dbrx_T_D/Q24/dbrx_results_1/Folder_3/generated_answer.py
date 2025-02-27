def sum_of_divisors_in_range(n):
    divisors = set()
    for i in range(1, int(n ** 0.5) + 1):
        if n % i:
            continue
        divisors.add(i)
        divisors.add(n // i)
    return sum((div for div in divisors if div >= 43 and div <= 46)) if divisors else 0