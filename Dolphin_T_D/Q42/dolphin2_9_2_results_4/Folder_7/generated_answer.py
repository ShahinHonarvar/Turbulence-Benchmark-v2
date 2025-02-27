def is_prime(n):
    if n == 2 or n == 3:
        return True
    if n < 2 or n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def prime_factors(lst):
    numbers = lst[851]
    factors = set()
    for i in range(2, numbers + 1):
        if numbers % i == 0 and is_prime(i):
            factors.add(i)
    return factors