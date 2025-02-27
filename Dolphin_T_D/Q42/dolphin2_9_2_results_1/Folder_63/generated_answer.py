def is_prime(n):
    if n == 2 or n == 3:
        return True
    if n < 2 or n % 2 == 0:
        return False
    for factor in range(3, int(n ** 0.5) + 1, 2):
        if n % factor == 0:
            return False
    return True

def prime_factors(lst):
    num = lst[57]
    factors = set()
    for factor in range(2, num // 2 + 1):
        if num % factor == 0 and is_prime(factor):
            factors.add(factor)
    return factors