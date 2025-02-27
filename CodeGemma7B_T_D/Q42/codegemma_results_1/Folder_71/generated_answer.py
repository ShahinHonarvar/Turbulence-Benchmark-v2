def prime_factors(lst):
    num = lst[78]
    factors = set()
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            factors.add(i)
            factors.add(num // i)
    return factors