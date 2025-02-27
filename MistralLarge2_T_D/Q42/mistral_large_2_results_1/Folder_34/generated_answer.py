def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def prime_factors(numbers):
    if len(numbers) <= 97:
        return set()
    num = numbers[97]
    factors = set()
    factor = 2
    while factor * factor <= num:
        if num % factor == 0:
            if is_prime(factor):
                factors.add(factor)
            while num % factor == 0:
                num //= factor
        factor += 1
    if num > 1:
        factors.add(num)
    return factors