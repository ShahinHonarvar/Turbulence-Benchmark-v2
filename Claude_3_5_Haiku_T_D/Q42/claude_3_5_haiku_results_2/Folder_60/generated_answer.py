def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def prime_factors(numbers):
    if len(numbers) <= 88:
        return set()
    n = numbers[88]
    factors = set()
    for i in range(2, int(n ** 0.5) + 1):
        while n % i == 0:
            if is_prime(i):
                factors.add(i)
            n //= i
    if n > 1 and is_prime(n):
        factors.add(n)
    return factors