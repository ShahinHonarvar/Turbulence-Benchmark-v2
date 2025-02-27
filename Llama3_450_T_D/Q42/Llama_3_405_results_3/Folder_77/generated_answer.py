def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def prime_factors(lst):
    n = lst[985]
    factors = set()
    for i in range(2, n + 1):
        while n % i == 0:
            factors.add(i)
            n = n // i
    return {f for f in factors if is_prime(f)}