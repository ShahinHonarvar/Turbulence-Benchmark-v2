def sum_of_divisors_in_range(n):
    divisors = set()
    for i in range(1, int(n ** 0.5) + 1):
        if n % i:
            continue
        divisors.add(i)
        divisors.add(n // i)
    divisors_in_range = divisors & set(range(27, 45))
    return sum(divisors_in_range)