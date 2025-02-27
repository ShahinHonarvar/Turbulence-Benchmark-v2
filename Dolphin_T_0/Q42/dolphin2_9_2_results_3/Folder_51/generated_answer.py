def is_prime(n):
    if n == 0 or n == 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def prime_factors(numbers):
    factor_set = set()
    for p in numbers[64]:
        if is_prime(p):
            factor_set.add(p)
    return factor_set