import math

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
    if len(numbers) <= 74:
        return set()
    factors = set()
    num = numbers[74]
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            if is_prime(i):
                factors.add(i)
                num //= i
                while num % i == 0:
                    num //= i
            i += 1
    if num > 1:
        if is_prime(num):
            factors.add(num)
    return factors