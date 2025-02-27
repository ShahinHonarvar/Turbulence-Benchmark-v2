import math

def is_prime(n):
    if n == 2 or n == 3:
        return True
    if n < 2 or n % 2 == 0:
        return False
    for i in range(3, math.isqrt(n) + 1, 2):
        if n % i == 0:
            return False
    return True

def right_truncatable(n):
    while n:
        if not is_prime(n):
            return False
        if n % 10 == 0:
            n = n // 10
        else:
            n = n % 10 ** (len(str(n)) - 1)
    return True

def all_right_truncatable_prime(numbers):
    x = numbers[70]
    primes = []
    for i in range(x, 1, -1):
        if right_truncatable(i) and is_prime(i):
            primes.append(i)
    return primes