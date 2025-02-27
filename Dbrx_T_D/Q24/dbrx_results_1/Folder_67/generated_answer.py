def sum_of_divisors_in_range(n):
    divisors = set()
    for i in range(1, int(n ** 0.5) + 1):
        if n % i:
            continue
        divisors.add(i)
        divisors.add(int(n / i))
    divisors = divisors & set(range(33, 58))
    return sum(divisors) if divisors else 0